import csv
import pandas as pd
from pathlib import Path
from typing import Dict, Any

from mir_converter.column_sanitizer import sanitize_columns


def convert_xlsx_to_csv(
    xlsx_path: str,
    csv_path: str,
    sheet_name=0,
    sanitize_columns_flag: bool = True,
) -> Dict[str, Any]:
    xlsx_path = Path(xlsx_path)
    csv_path = Path(csv_path)

    df = pd.read_excel(
        xlsx_path,
        sheet_name=sheet_name,
        engine="openpyxl",
        dtype=str,
    )

    column_mapping = {}

    if sanitize_columns_flag:
        column_mapping = sanitize_columns(df.columns.tolist())
        df = df.rename(columns=column_mapping)

    df.to_csv(
        csv_path,
        index=False,
        encoding="utf-8",
        quoting=csv.QUOTE_ALL,
        lineterminator="\n",
    )

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "output": str(csv_path),
        "column_mapping": column_mapping,
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Excel (.xlsx) to Spark-safe CSV"
    )
    parser.add_argument("xlsx", help="Input Excel file")
    parser.add_argument("csv", help="Output CSV file")
    parser.add_argument("--sheet", default=0)
    parser.add_argument(
        "--no-sanitize-columns",
        action="store_true",
        help="Disable column name sanitization",
    )

    args = parser.parse_args()

    result = convert_xlsx_to_csv(
        args.xlsx,
        args.csv,
        sheet_name=args.sheet,
        sanitize_columns_flag=not args.no_sanitize_columns,
    )

    print(result)


if __name__ == "__main__":
    main()
