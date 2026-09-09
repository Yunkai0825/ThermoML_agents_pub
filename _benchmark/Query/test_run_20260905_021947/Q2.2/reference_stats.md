# Reference Stats — query-agent

**Run started:** 2026-09-05 05:26:19
**Wall time (at last flush):** 145.7 s

---

## 1. Argo API Call Summary

| Tier | Calls | System (chars) | Prompt (chars) | Response (chars) | Total sent | Avg Context | Total time (s) | Model(s) |
|------|------:|---------------:|---------------:|-----------------:|-----------:|------------:|---------------:|----------|
| L0-main | 9 | 29,806 | 32,797 | 11,827 | 62,603 | 6,955 | 73.7 | claudeopus46 |
| L1-worker | 15 | 138,714 | 36,775 | 13,226 | 175,489 | 11,699 | 95.0 | claudeopus46 |
| **TOTAL** | **24** | **168,520** | **69,572** | **25,053** | **238,092** | **9,920** | **168.7** | |

**Estimated tokens:** ~59,523 input + ~6,263 output = ~65,786 total
*(rough estimate: 1 token ≈ 4 chars)*

---

## 2. Data Complexity Summary

### 2a. Raw Tool-Return Counters

*Direct counts from raw tool results, before agent condensation.*

| Tool | Compounds | Properties | Variables | Constraints | DOIs | Blocks | Datapoints |
|------|----------:|-----------:|----------:|------------:|-----:|-------:|-----------:|
| `resolve_ids` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `search_system_summary` | 0 | 1 | 0 | 0 | 1176 | 3294 | 137,229 |
| `search_system_summary` | 0 | 1 | 0 | 0 | 429 | 1081 | 81,066 |
| **TOTAL** | **0** | **2** | **0** | **0** | **1605** | **4375** | **218,295** |

### 2b. Agent-Condensed Data Complexity

*Deduplicated entities and DOI references after agent processing.*

#### Phases (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBphase_1 |  | resolve_ids |

#### Properties (1 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBprop_4 |  | search_system_summary |

#### References (39 unique)

| ID | Name | Source tools |
|---:|------|-------------|
| GLOBlit_7152 |  | search_system_summary |
| GLOBlit_3363 |  | search_system_summary |
| GLOBlit_5017 |  | search_system_summary |
| GLOBlit_6843 |  | search_system_summary |
| GLOBlit_6965 |  | search_system_summary |
| GLOBlit_7034 |  | search_system_summary |
| GLOBlit_6861 |  | search_system_summary |
| GLOBlit_8239 |  | search_system_summary |
| GLOBlit_7525 |  | search_system_summary |
| GLOBlit_10467 |  | search_system_summary |
| GLOBlit_2316 |  | search_system_summary |
| GLOBlit_145 |  | search_system_summary |
| GLOBlit_8502 |  | search_system_summary |
| GLOBlit_4955 |  | search_system_summary |
| GLOBlit_4746 |  | search_system_summary |
| GLOBlit_7691 |  | search_system_summary |
| GLOBlit_6743 |  | search_system_summary |
| GLOBlit_7492 |  | search_system_summary |
| GLOBlit_8755 |  | search_system_summary |
| GLOBlit_8761 |  | search_system_summary |
| GLOBlit_10411 |  | search_system_summary |
| GLOBlit_10589 |  | search_system_summary |
| GLOBlit_7366 |  | search_system_summary |
| GLOBlit_4756 |  | search_system_summary |
| GLOBlit_11136 |  | search_system_summary |
| GLOBlit_4672 |  | search_system_summary |
| GLOBlit_6768 |  | search_system_summary |
| GLOBlit_10530 |  | search_system_summary |
| GLOBlit_10142 |  | search_system_summary |
| GLOBlit_3565 |  | search_system_summary |
| GLOBlit_4565 |  | search_system_summary |
| GLOBlit_10680 |  | search_system_summary |
| GLOBlit_6135 |  | search_system_summary |
| GLOBlit_4972 |  | search_system_summary |
| GLOBlit_4043 |  | search_system_summary |
| GLOBlit_4523 |  | search_system_summary |
| GLOBlit_7006 |  | search_system_summary |
| GLOBlit_10310 |  | search_system_summary |
| GLOBlit_5051 |  | search_system_summary |

#### Aggregate Counts (Condensed)

| Metric | Count |
|--------|------:|
| Unique Phases | 1 |
| Unique Properties | 1 |
| Unique References | 39 |
| Total DOIs | 0 |
| Unique parent blocks | 0 |
| Explicit block/subsystem targets | 0 |
| Subsystem targets | 0 |
| Target-matched data points | 0 |

---

## 3. DOI & Block References

*(no DOI/block references recorded)*

---

## 4. Tool Results (post tool-pipeline, pre context-compaction)

| # | Iter | Tool | Args | Result (chars) | Subagent | Out (chars) | Time (s) |
|--:|-----:|------|------|------------:|----------|------------:|---------:|
| 1 | 1 | `resolve_ids` | entity_type=phase, purpose=Resolve liquid phase ID… | 197 | KEEP ←in 212 | 197 | 3.5 |
| 2 | 3 | `search_system_summary` | limit=20, property=GLOBprop_4, purpose=Count binar… | 861 | KEEP ←in 796 | 861 | 9.2 |
| 3 | 4 | `search_system_summary` | limit=20, property=GLOBprop_4, purpose=Compare ter… | 573 | KEEP ←in 787 | 573 | 6.7 |
| 4 | 1 | `L1_query` | id_catalog=GLOBprop_4 = Viscosity (dynam…, instruc… | 4,552 | — | — | 82.8 |
| | | **TOTAL (4 tools)** | | **6,183** | | **1,631** | **102.2** |

---

## 5. Compaction Events

*(no compaction events recorded)*

---

## 6. Argo Call Detail Log

| # | Tier | Model | System | Prompt | Context | Response | Time (s) |
|--:|------|-------|-------:|-------:|--------:|---------:|---------:|
| 1 | L0-main | claudeopus46 | 11,581 | 663 | 12,244 | 1,545 | 10.5 |
| 2 | L1-worker | claudeopus46 | 24,095 | 1,317 | 25,412 | 947 | 6.8 |
| 3 | L1-worker | claudeopus46 | 3,767 | 361 | 4,128 | 306 | 3.4 |
| 4 | L1-worker | claudeopus46 | 24,095 | 1,823 | 25,918 | 691 | 9.5 |
| 5 | L1-worker | claudeopus46 | 24,095 | 2,902 | 26,997 | 625 | 4.1 |
| 6 | L1-worker | claudeopus46 | 3,767 | 1,234 | 5,001 | 1,141 | 8.1 |
| 7 | L1-worker | claudeopus46 | 24,095 | 3,165 | 27,260 | 628 | 5.1 |
| 8 | L1-worker | claudeopus46 | 3,767 | 1,236 | 5,003 | 870 | 6.2 |
| 9 | L1-worker | claudeopus46 | 24,095 | 4,064 | 28,159 | 3,453 | 21.8 |
| 10 | L1-worker | claudeopus46 | 2,106 | 4,186 | 6,292 | 561 | 4.0 |
| 11 | L1-worker | claudeopus46 | 627 | 2,628 | 3,255 | 882 | 5.6 |
| 12 | L1-worker | claudeopus46 | 366 | 1,338 | 1,704 | 77 | 1.9 |
| 13 | L1-worker | claudeopus46 | 2,320 | 2,748 | 5,068 | 912 | 6.1 |
| 14 | L1-worker | claudeopus46 | 366 | 1,293 | 1,659 | 869 | 3.9 |
| 15 | L1-worker | claudeopus46 | 366 | 1,349 | 1,715 | 867 | 3.6 |
| 16 | L1-worker | claudeopus46 | 787 | 7,131 | 7,918 | 397 | 4.9 |
| 17 | L0-main | claudeopus46 | 11,581 | 10,648 | 22,229 | 4,554 | 30.2 |
| 18 | L0-main | claudeopus46 | 2,106 | 4,105 | 6,211 | 1,000 | 7.1 |
| 19 | L0-main | claudeopus46 | 2,320 | 3,610 | 5,930 | 1,328 | 7.1 |
| 20 | L0-main | claudeopus46 | 366 | 1,803 | 2,169 | 1,284 | 4.2 |
| 21 | L0-main | claudeopus46 | 366 | 1,549 | 1,915 | 1,292 | 5.1 |
| 22 | L0-main | claudeopus46 | 560 | 4,912 | 5,472 | 260 | 2.6 |
| 23 | L0-main | claudeopus46 | 560 | 4,376 | 4,936 | 549 | 5.2 |
| 24 | L0-main | claudeopus46 | 366 | 1,131 | 1,497 | 15 | 1.7 |

