"""Read numbers from CSV files."""

import csv


def read_column(path, name):
    """Read one column of a CSV file with a header row, as floats.

    Empty cells are skiped.
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if name not in (reader.fieldnames or []):
            raise KeyError(f"no column {name!r} in {path}")
        return [float(row[name]) for row in reader if row[name].strip()]
