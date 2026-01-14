import csv
import pandas as pd
from pathlib import Path
import argparse


def convert_xlsx_to_csv(
    xlsx_path: str,
    csv_path: str,
    sheet_name=0,
):
    xlsx_path = Path(xlsx_path)
    csv_path = Path(csv_path)

    df = pd.read_excel(
        xlsx_path,
        sheet_name=sheet_name,
        engine="openpyxl",
        dtype=str,
    )

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
    }


def main():
    parser = argparse.ArgumentParser(
        description="Convert Excel (.xlsx) to Spark-safe CSV"
    )
    parser.add_argument("xlsx", help="Input Excel file")
    parser.add_argument("csv", help="Output CSV file")
    parser.add_argument("--sheet", default=0)

    args = parser.parse_args()

    result = convert_xlsx_to_csv(
        args.xlsx,
        args.csv,
        sheet_name=args.sheet,
    )

    print(result)


if __name__ == "__main__":
    main()
