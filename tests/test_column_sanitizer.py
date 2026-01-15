from mir_converter.column_sanitizer import sanitize_column_name


def test_sanitize_column_name():
    assert sanitize_column_name("Case No.") == "case_no"
    assert sanitize_column_name("Case-No") == "case_no"
    assert sanitize_column_name(" Adverse Event (Serious) ") == "adverse_event_serious"

