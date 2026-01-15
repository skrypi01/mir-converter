import re
from typing import Dict, List


INVALID_CHARS_PATTERN = re.compile(r"[ ,.;{}()\n\t=]")


def sanitize_column_name(col: str) -> str:
    """
    Sanitize a column name to be Delta / Unity Catalog safe.

    Rules:
    - Replace invalid characters with underscore
    - Collapse multiple underscores
    - Strip leading/trailing underscores
    """
    col = INVALID_CHARS_PATTERN.sub("_", col)
    col = re.sub(r"_+", "_", col)
    col = col.strip("_")
    return col


def sanitize_columns(columns: List[str]) -> Dict[str, str]:
    """
    Return a mapping of original -> sanitized column names.
    """
    mapping = {}
    for col in columns:
        new_col = sanitize_column_name(col)
        mapping[col] = new_col
    return mapping
