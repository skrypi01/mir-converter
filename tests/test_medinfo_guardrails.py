import os
import pytest
from mir_converter import convert_xlsx_to_csv

@pytest.mark.skipif(
    not os.environ.get("MEDINFO_XLSX"),
    reason="No MedInfo file provided"
)
def test_medinfo_row_count():
    xlsx_path = os.environ["MEDINFO_XLSX"]
    csv_path = "../mir_converter_guardrails_test_out.csv"

    result = convert_xlsx_to_csv(xlsx_path, csv_path)

    assert result["rows"] >= 4000
