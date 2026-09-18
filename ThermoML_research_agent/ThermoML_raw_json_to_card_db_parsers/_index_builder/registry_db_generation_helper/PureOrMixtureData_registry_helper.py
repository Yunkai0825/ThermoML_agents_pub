"""Build the strict PureOrMixtureData block registry from PCS cards."""

from __future__ import annotations

import os

from ThermoML_raw_json_to_card_db_parsers._index_builder.registry_db_generation_helper.registry_projection import (
    PCS_DB,
    ROOT,
    build_registry,
)


OUTPUT_DB = os.path.join(ROOT, "card_databases_storage", "PureOrMixtureData_registry.db")


def build_pom_registry(pcs_db=PCS_DB, output_db=OUTPUT_DB):
    print("Building strict PureOrMixtureData registry")
    print(f"  PCS DB : {pcs_db}")
    print(f"  Output : {output_db}")
    count = build_registry(
        block_type="PureOrMixtureData", output_db=output_db, pcs_db=pcs_db
    )
    print(f"  Done: {count:,} property blocks")
    return count


if __name__ == "__main__":
    build_pom_registry()
