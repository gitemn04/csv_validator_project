# Validation module for pharmaceutical CSV datasets
import os

def validate_filename(filename):
    if filename.startswith("MED_DATA_") and filename.endswith(".csv"):
        return True
    else:
        return False


def validate_empty_file(filepath):
    if os.path.getsize(filepath) == 0:
        return False
    else:
        return True


def validate_headers(header_line):
    expected_headers = ["batch", "timestamp", "value"]

    headers = header_line.strip().split(",")

    if headers == expected_headers:
        return True
    else:
        return False
    
def validate_column_count(row):
    columns = row.strip().split(",")

    if len(columns) == 3:
        return True
    else:
        return False
    
def validate_numeric_value(row):
    columns = row.strip().split(",")

    try:
        float(columns[2])
        return True
    except:
        return False
    
    
def validate_row(row):
    if not validate_column_count(row):
        return False
    
    if not validate_numeric_value(row):
        return False

    return True