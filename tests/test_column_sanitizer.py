from mir_converter.column_sanitizer import sanitize_column_name


def test_sanitize_column_name():
    assert sanitize_column_name("Case No.") == "Case_No"
    assert sanitize_column_name("Adverse Event (Serious)") == "Adverse_Event_Serious"
    assert sanitize_column_name(" Product  Name ") == "Product_Name"
