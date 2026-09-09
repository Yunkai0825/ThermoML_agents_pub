"""Build the strict, global-ID keyed PCS property knowledge database."""

import copy
import json
import os
import sqlite3
import time

from ThermoML_raw_json_to_card_db_parsers.id_schema import global_ordinal
from ThermoML_raw_json_to_card_db_parsers.index_lookup import ThermoMLIndex


_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_CARDS_DIR = os.path.join(
    _ROOT, "card_databases_storage", "_card_schemas", "_core_data_cards_schema",
    "Property_Card_Schema", "PCS_ID_and_DK_cards",
)
_DB_PATH = os.path.join(
    _ROOT, "card_databases_storage", "Individual_cards_dbs", "PCS_ID_DK.db"
)


def _load_dk_cards():
    """Load authored DK cards keyed by their global base property slug."""
    cards = {}
    unreadable = []
    for group_name in sorted(os.listdir(_CARDS_DIR)):
        group_dir = os.path.join(_CARDS_DIR, group_name)
        if not os.path.isdir(group_dir):
            continue
        for filename in sorted(os.listdir(group_dir)):
            if not filename.endswith(".json"):
                continue
            path = os.path.join(group_dir, filename)
            try:
                with open(path, encoding="utf-8") as handle:
                    card = json.load(handle)
                base_prop_id = card["prop_ID"]
                if base_prop_id in cards:
                    raise ValueError(f"duplicate authored prop_ID {base_prop_id!r}")
                cards[base_prop_id] = card
            except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
                unreadable.append((path, str(exc)))
    if unreadable:
        raise RuntimeError(f"Unreadable PCS DK cards: {unreadable[:10]!r}")
    return cards


def _project_registry_card(row, authored):
    """Project one canonical registry row into exactly one ID/DK card."""
    base_prop_id = ThermoMLIndex.base_id(row["prop_id"])
    if authored is None:
        card = {
            "card_type": "registry_stub",
            "identity": {
                "name": row["prop_name"],
                "thermoml_name": row["prop_name"],
                "property_group": row["prop_group"],
            },
            "domain_knowledge": None,
        }
    else:
        card = copy.deepcopy(authored)
        card["card_type"] = "domain_knowledge"

    # The top-level identity is the canonical global occurrence type.  A
    # component-aware template and its plain counterpart therefore receive
    # distinct cards and distinct GLOBprop_* IDs even when they share DK text.
    card["prop_num_id"] = row["prop_num_id"]
    card["prop_ID"] = row["prop_id"]
    card["base_prop_ID"] = base_prop_id
    card["component_linked"] = bool(row["comp_id_linked"])
    return card


def build_db(verbose=True):
    os.makedirs(os.path.dirname(_DB_PATH), exist_ok=True)
    staging = _DB_PATH + ".building"
    for suffix in ("", "-wal", "-shm"):
        path = staging + suffix
        if os.path.exists(path):
            os.remove(path)

    t0 = time.time()
    index = ThermoMLIndex()
    authored_by_base = _load_dk_cards()
    registry_rows = sorted(
        index._property_by_name.values(),
        key=lambda row: global_ordinal("prop_num_id", row["prop_num_id"]),
    )
    registry_bases = {ThermoMLIndex.base_id(row["prop_id"]) for row in registry_rows}
    authored_without_registry = sorted(set(authored_by_base) - registry_bases)
    if authored_without_registry:
        raise RuntimeError(
            f"PCS DK prop_ID values absent from canonical registry: {authored_without_registry!r}"
        )

    conn = sqlite3.connect(staging)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript("""
        CREATE TABLE cards (
            prop_num_id          TEXT PRIMARY KEY,
            prop_id              TEXT NOT NULL UNIQUE,
            base_prop_id         TEXT NOT NULL,
            prop_group           TEXT,
            prop_name            TEXT,
            component_linked     INTEGER NOT NULL,
            has_domain_knowledge INTEGER NOT NULL,
            json_data            TEXT NOT NULL
        );
        CREATE INDEX idx_cards_prop_id ON cards(prop_id);
        CREATE INDEX idx_cards_base ON cards(base_prop_id);
        CREATE INDEX idx_cards_group ON cards(prop_group);
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    """)

    rich = stubs = 0
    for row in registry_rows:
        base_prop_id = ThermoMLIndex.base_id(row["prop_id"])
        authored = authored_by_base.get(base_prop_id)
        card = _project_registry_card(row, authored)
        has_dk = int(authored is not None)
        rich += has_dk
        stubs += 1 - has_dk
        conn.execute(
            "INSERT INTO cards VALUES (?,?,?,?,?,?,?,?)",
            (row["prop_num_id"], row["prop_id"], base_prop_id,
             row["prop_group"], row["prop_name"], int(row["comp_id_linked"]),
             has_dk, json.dumps(card, ensure_ascii=False)),
        )

    elapsed = time.time() - t0
    metadata = {
        "id_schema": "prefixed-v2",
        "total_cards": str(len(registry_rows)),
        "domain_knowledge_cards": str(rich),
        "registry_stub_cards": str(stubs),
        "authored_base_cards": str(len(authored_by_base)),
        "build_time_sec": f"{elapsed:.2f}",
    }
    conn.executemany("INSERT INTO metadata VALUES (?,?)", metadata.items())
    conn.commit()
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()
    os.replace(staging, _DB_PATH)

    if verbose:
        print(f"PCS_ID_DK: {len(registry_rows)} global cards ({rich} DK, {stubs} stubs)")
        print(f"Published atomically: {_DB_PATH}")
    return _DB_PATH


if __name__ == "__main__":
    build_db()
