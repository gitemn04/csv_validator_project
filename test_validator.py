# Unit tests for the CSV validation module
import os
from validator import validate_filename
from validator import validate_empty_file


def test_invalid_filename():
    filename = "MEDDATA_20230603140104.csv"
    assert validate_filename(filename) == False


def test_empty_file():
    filename = "empty_test.csv"

    open(filename, "w").close()

    assert validate_empty_file(filename) == False

    os.remove(filename)
    
from validator import validate_headers

def test_invalid_headers():
    header = "batch,time,value"
    assert validate_headers(header) == False
    
    
from validator import validate_column_count

def test_invalid_column_count():
    row = "1,2023-06-03T14:01:04"
    assert validate_column_count(row) == False
    
    
from validator import validate_numeric_value

def test_invalid_numeric_value():
    row = "1,2023-06-03T14:01:04,abc"
    assert validate_numeric_value(row) == False
    
    
from validator import validate_row

def test_valid_row():
    row = "1,2023-06-03T14:01:04,9.1"
    assert validate_row(row) == True