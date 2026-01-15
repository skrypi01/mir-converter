# MIR Excel → CSV Converter

Deterministic, Spark-safe Excel (`.xlsx`) → CSV converter for long-text
Medical Information (MIR) data.

This tool is designed to eliminate Excel-related ingestion issues
(filters, hidden rows, broken quoting, multiline text, invalid column
names) **before loading data into Databricks / Unity Catalog**.

---

## Key Features

- Reliable Excel `.xlsx` reading (ignores Excel filters & views)
- UTF-8 CSV output
- Quotes **all fields** (Spark-safe)
- Preserves multiline text
- Deterministic row / column counts
- **Automatic column name sanitization**
  - enforced `snake_case`
  - lowercase
  - Unity Catalog / Delta-safe
- **Collision detection** (fails fast on ambiguous columns)
- **Warnings emitted when column names change**
- **Column-mapping persisted as JSON** (governance-ready)
- CLI + Python API
- Unit tests + real-data guardrail tests

---

## Column Sanitization (IMPORTANT)

All column names are sanitized **by default** to comply with
Delta Lake / Unity Catalog constraints.

### Sanitization rules

| Rule | Example |
|----|----|
| Lowercase | `Case No.` → `case_no` |
| Replace invalid characters with `_` | `Adverse Event (Serious)` → `adverse_event_serious` |
| Collapse multiple underscores | `Product__Name` → `product_name` |
| Strip leading / trailing underscores | `_Case_No_` → `case_no` |

### Collision detection (hard stop)

If two original columns sanitize to the same name, the converter **fails**:


---

## Prerequisites

- Windows
- Python **3.9+**
- VS Code (recommended)

---

## Project structure (important)

dev/converter/
├── src/
│   └── mir_converter/
│       ├── __init__.py
│       ├── xlsx_to_csv.py
│       └── column_sanitizer.py
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
