import csv
from pathlib import Path
import pandas as pd
import pytest

from mir_converter.xlsx_to_csv import convert_xlsx_to_csv


def create_sample_xlsx(path: Path):
    """Create a small Excel file with edge cases."""
    df = pd.DataFrame(
        {
            "Question": [
                "What is X?",
                "Text with, comma",
                "Multiline\ntext"
            ],
            "Response": [
                "Simple answer",
                "Quoted \"text\" here",
                "Another\nlong\nanswer"
            ],
            "Score": ["0.9", "0.8", "0.7"]
        }
    )

    df.to_excel(path, index=False, engine="openpyxl")



def test_convert_xlsx_to_csv(tmp_path):
    xlsx_path = tmp_path / "input.xlsx"
    csv_path = tmp_path / "output.csv"

    create_sample_xlsx(xlsx_path)

    with pytest.warns(UserWarning, match="Sanitized column names"):
        result = convert_xlsx_to_csv(xlsx_path, csv_path)


    # Assert: metadata
    assert result["rows"] == 3
    assert result["columns"] == 3
    assert csv_path.exists()

    # Assert: CSV integrity
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Header + 3 rows
    assert len(rows) == 4
    assert rows[0] == ["question", "response", "score"]

    # Check quoting and multiline preservation
    assert "Text with, comma" in rows[2][0]
    assert "Multiline\ntext" in rows[3][0]
    assert "Quoted \"text\" here" in rows[2][1]

def test_expected_row_count(tmp_path):
    xlsx_path = tmp_path / "input.xlsx"
    csv_path = tmp_path / "output.csv"

    create_sample_xlsx(xlsx_path)

    result = convert_xlsx_to_csv(xlsx_path, csv_path)

    assert result["rows"] == 3
    assert result["columns"] == 3

