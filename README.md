# MIR Excel → CSV Converter

Deterministic, Spark-safe Excel (`.xlsx`) → CSV converter for long-text
Medical Information (MIR) data.

This tool is designed to eliminate Excel-related ingestion issues
(filters, hidden rows, broken quoting, multiline text) before loading
data into Databricks / Unity Catalog.

---

## Features

- Reads Excel `.xlsx` reliably (ignores Excel filters & views)
- Outputs UTF-8 CSV
- Quotes **all fields** (safe for Spark)
- Preserves multiline text
- Deterministic row / column counts
- CLI + Python API
- Unit tested

---

## Prerequisites

- Windows
- Python **3.9+**
- VS Code (recommended)

---

## Project structure (important)

```text
dev/converter/
├── src/
│   └── mir_converter/
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
