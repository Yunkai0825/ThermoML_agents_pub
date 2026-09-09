# Block-Centric Search Tools

Multi-DB query functions that start from a block and fetch related cards.
Used primarily by L2 leaf evaluators to gather context about a specific block.

## Functions

| File | Function | Fetches |
|------|----------|---------|
| `search_comp_INDIV_and_DK_from_block.py` | `search_comp_from_block()` | Compound DK + INDIV cards for all compounds in a block |
| `search_meas_INDIV_and_DK_from_block.py` | `search_meas_from_block()` | Measurement DK + INDIV cards for the block's method |
| `search_prop_DK_from_block.py` | `search_prop_dk_from_block()` | Property DK cards for the block's properties |
| `search_reference_from_block.py` | `search_ref_from_block()` | Reference card for the block's DOI |

## Usage

```python
from block_centric_search_tools.search_comp_INDIV_and_DK_from_block import search_comp_from_block

result = search_comp_from_block(doi="10.1016/j.fluid.2014.11.020", block_number=3)
# → compound cards for all compounds in block 3
```
