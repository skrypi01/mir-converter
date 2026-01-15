import re
from typing import Dict, List, Tuple

# Allow only letters, numbers, underscore
INVALID_CHARS_PATTERN = re.compile(r"[^A-Za-z0-9]+")


def sanitize_column_name(col: str) -> str:
    """
    Convert column name to snake_case, lowercase, UC-safe.
    """
    col = col.strip()
    col = INVALID_CHARS_PATTERN.sub("_", col)
    col = re.sub(r"_+", "_", col)
    col = col.strip("_")
    return col.lower()

def sanitize_columns(columns: List[str]) -> Tuple[Dict[str, str], Dict[str, List[str]]]:
    """
    Returns:
      - mapping: original -> sanitized
      - collisions: sanitized -> list of originals (only if >1)
    """
    mapping = {}
    reverse = {}

    for col in columns:
        new_col = sanitize_column_name(col)
        mapping[col] = new_col
        reverse.setdefault(new_col, []).append(col)

    collisions = {k: v for k, v in reverse.items() if len(v) > 1}
    return mapping, collisions
