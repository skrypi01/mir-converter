import csv
import pandas as pd
from pathlib import Path
from typing import Dict, Any
import warnings
from mir_converter.column_sanitizer import sanitize_columns
import json
from datetime import datetime

#warnings.simplefilter(action="ignore", category=UserWarning)



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
    collisions = {}

    if sanitize_columns_flag:
        column_mapping, collisions = sanitize_columns(df.columns.tolist())

        # Collision detection
        if collisions:
            raise ValueError(
                f"Column name collision after sanitization: {collisions}"
            )

        #  Warn if columns were changed
        changed = {
            k: v for k, v in column_mapping.items() if k != v
        }
        if changed:
            warnings.warn(
                f"Sanitized column names: {changed}",
                UserWarning
            )
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
    
    mapping_payload = {
        "version": "v1",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "column_mapping": column_mapping,
    }

    mapping_path = csv_path.with_suffix(".columns.json")

    with open(mapping_path, "w", encoding="utf-8") as f:
        json.dump(mapping_payload, f, indent=2)


if __name__ == "__main__":
    main()
