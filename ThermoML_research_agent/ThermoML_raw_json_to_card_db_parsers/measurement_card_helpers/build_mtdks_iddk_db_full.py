"""Build one strict MTDKS ID/DK card per global measurement type."""

import copy
import csv
import json
import os
import sqlite3
import time

from ThermoML_raw_json_to_card_db_parsers.id_schema import global_ordinal, require_global_id


_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_CARDS_DIR = os.path.join(
    _ROOT, "card_databases_storage", "ID_and_DK_cards_raw_json",
    "Meas_ID_and_DK_cards",
)
_CSV_DIR = os.path.join(
    _ROOT, "ThermoML_raw_json_to_card_db_parsers", "_index_builder", "id_name_lists"
)
_RAW_DB = os.path.join(_ROOT, "ThermoML.v2020-09-30.db", "thermoml_raw.db")
_DB_PATH = os.path.join(
    _ROOT, "card_databases_storage", "Individual_cards_dbs", "MTDKS_ID_DK.db"
)


def _read_csv(filename):
    with open(os.path.join(_CSV_DIR, filename), encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _load_registry():
    rows = _read_csv("measurement_ids.csv")
    by_slug = {}
    for row in rows:
        row["meas_num_id"] = require_global_id("meas_num_id", row["meas_num_id"])
        row["n_blocks"] = int(row["n_blocks"])
        row["n_aliases"] = int(row.get("n_aliases") or 0)
        by_slug[row["meas_id"]] = row

    aliases_by_slug = {slug: [] for slug in by_slug}
    alias_to_slug = {}
    for alias in _read_csv("measurement_aliases.csv"):
        gid = require_global_id("meas_num_id", alias["meas_num_id"])
        canonical = by_slug.get(alias["meas_id"])
        if canonical is None or canonical["meas_num_id"] != gid:
            raise RuntimeError(f"Broken measurement alias row: {alias!r}")
        aliases_by_slug[alias["meas_id"]].append(alias)
        prior = alias_to_slug.setdefault(alias["source_method_name"], alias["meas_id"])
        if prior != alias["meas_id"]:
            raise RuntimeError(
                f"Exact method label maps to multiple global types: {alias['source_method_name']!r}"
            )
    return rows, by_slug, aliases_by_slug, alias_to_slug


def _load_authored_cards():
    cards = {}
    for family in sorted(os.listdir(_CARDS_DIR)):
        family_dir = os.path.join(_CARDS_DIR, family)
        if not os.path.isdir(family_dir):
            continue
        for filename in sorted(os.listdir(family_dir)):
            if not filename.endswith(".json"):
                continue
            path = os.path.join(family_dir, filename)
            with open(path, encoding="utf-8") as handle:
                card = json.load(handle)
            meas_id = card["meas_ID"]
            if meas_id in cards:
                raise RuntimeError(f"Duplicate authored meas_ID {meas_id!r}")
            cards[meas_id] = card
    return cards


def _load_usage(alias_to_slug):
    """Aggregate raw usage by canonical global type without alias double counting."""
    stats = {}
    conn = sqlite3.connect(f"file:{_RAW_DB}?mode=ro", uri=True)
    rows = conn.execute("""
        SELECT method_name, doi, prop_group, COUNT(*)
        FROM block_properties
        WHERE method_name IS NOT NULL
        GROUP BY method_name, doi, prop_group
    """)
    for method_name, doi, prop_group, count in rows:
        slug = alias_to_slug.get(method_name)
        if slug is None:
            raise RuntimeError(f"Raw method label absent from alias registry: {method_name!r}")
        item = stats.setdefault(slug, {"instances": 0, "papers": set(), "groups": {}})
        item["instances"] += count
        item["papers"].add(doi)
        group = item["groups"].setdefault(
            prop_group or "", {"instances": 0, "papers": set()}
        )
        group["instances"] += count
        group["papers"].add(doi)
    conn.close()
    return stats


def _usage_json(item):
    item = item or {"instances": 0, "papers": set(), "groups": {}}
    return {
        "instance_count": item["instances"],
        "n_papers": len(item["papers"]),
        "property_groups": sorted(group for group in item["groups"] if group),
        "per_group": {
            group: {"instances": value["instances"], "papers": len(value["papers"])}
            for group, value in sorted(item["groups"].items())
        },
    }


def _project_card(row, aliases, usage, authored):
    if authored is None:
        card = {
            "card_type": "registry_stub",
            "identity": {
                "name": row["method_name"],
                "measurement_family": (
                    "Standard" if row["method_type"] == "standard" else "Custom"
                ),
            },
            "domain_knowledge": None,
        }
    else:
        card = copy.deepcopy(authored)
        card["card_type"] = "standard_dk"

    card["meas_ID"] = row["meas_id"]
    card["meas_num_id"] = row["meas_num_id"]
    identity = card.setdefault("identity", {})
    identity["canonical_method_name"] = row["method_name"]
    identity["source_aliases"] = [
        {
            "name": alias["source_method_name"],
            "method_type": alias["source_method_type"],
        }
        for alias in sorted(
            aliases, key=lambda value: (
                value["source_method_name"], value["source_method_type"]
            )
        )
    ]
    identity["db_usage"] = _usage_json(usage)
    return card


def build_db():
    t0 = time.time()
    os.makedirs(os.path.dirname(_DB_PATH), exist_ok=True)
    staging = _DB_PATH + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging + suffix
        if os.path.exists(path):
            os.remove(path)

    registry, by_slug, aliases_by_slug, alias_to_slug = _load_registry()
    authored = _load_authored_cards()
    authored_without_registry = sorted(set(authored) - set(by_slug))
    if authored_without_registry:
        raise RuntimeError(
            f"Authored MTDKS IDs absent from registry: {authored_without_registry!r}"
        )
    usage = _load_usage(alias_to_slug)

    conn = sqlite3.connect(staging)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript("""
        CREATE TABLE cards (
            meas_num_id         TEXT PRIMARY KEY,
            meas_id             TEXT NOT NULL UNIQUE,
            method_name         TEXT NOT NULL,
            method_type         TEXT NOT NULL,
            card_type           TEXT NOT NULL,
            has_domain_knowledge INTEGER NOT NULL,
            json_data           TEXT NOT NULL
        );
        CREATE INDEX idx_cards_meas_id ON cards(meas_id);
        CREATE INDEX idx_cards_method_type ON cards(method_type);
        CREATE TABLE measurement_aliases (
            source_method_name TEXT NOT NULL,
            source_method_type TEXT NOT NULL,
            meas_num_id TEXT NOT NULL,
            meas_id TEXT NOT NULL,
            n_blocks INTEGER,
            PRIMARY KEY (source_method_name, source_method_type),
            FOREIGN KEY (meas_num_id) REFERENCES cards(meas_num_id)
        );
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    """)

    rich = 0
    for row in sorted(
        registry,
        key=lambda value: global_ordinal("meas_num_id", value["meas_num_id"]),
    ):
        source = authored.get(row["meas_id"])
        card = _project_card(
            row, aliases_by_slug[row["meas_id"]], usage.get(row["meas_id"]), source
        )
        has_dk = int(source is not None)
        rich += has_dk
        conn.execute(
            "INSERT INTO cards VALUES (?,?,?,?,?,?,?)",
            (row["meas_num_id"], row["meas_id"], row["method_name"],
             row["method_type"], card["card_type"], has_dk,
             json.dumps(card, ensure_ascii=False)),
        )

    for aliases in aliases_by_slug.values():
        for alias in aliases:
            conn.execute(
                "INSERT INTO measurement_aliases VALUES (?,?,?,?,?)",
                (alias["source_method_name"], alias["source_method_type"],
                 alias["meas_num_id"], alias["meas_id"], int(alias["n_blocks"])),
            )

    elapsed = time.time() - t0
    metadata = {
        "id_schema": "prefixed-v2",
        "total_cards": str(len(registry)),
        "domain_knowledge_cards": str(rich),
        "registry_stub_cards": str(len(registry) - rich),
        "total_aliases": str(sum(map(len, aliases_by_slug.values()))),
        "build_time_sec": f"{elapsed:.2f}",
    }
    conn.executemany("INSERT INTO metadata VALUES (?,?)", metadata.items())
    conn.commit()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()
    os.replace(staging, _DB_PATH)
    print(
        f"MTDKS_ID_DK: {len(registry)} global cards, {rich} DK, "
        f"{len(registry)-rich} stubs, {sum(map(len, aliases_by_slug.values()))} aliases"
    )
    print(f"Published atomically: {_DB_PATH}")
    return _DB_PATH


if __name__ == "__main__":
    build_db()
