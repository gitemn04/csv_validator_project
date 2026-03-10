from validator import *
from logger import Logger
from csv_generator import generate_valid_csv, generate_invalid_csv

# Initialize logger
logger = Logger()

# Generate sample CSV files for testing
generate_valid_csv("valid_pharma_data.csv")
generate_invalid_csv("invalid_pharma_data.csv")

files = ["valid_pharma_data.csv", "invalid_pharma_data.csv"]

for file in files:

    print("Checking file:", file)

    # Validate filename
    if not validate_filename(file):
        logger.log_error(f"{file} -> Invalid filename")
        continue

    # Validate file is not empty
    if not validate_empty_file(file):
        logger.log_error(f"{file} -> File is empty")
        continue

    with open(file, "r") as f:

        header = f.readline()

        # Validate headers
        if not validate_headers(header):
            logger.log_error(f"{file} -> Invalid headers")
            continue

        # Validate each row
        for row in f:
            if not validate_row(row):
                logger.log_error(f"{file} -> Invalid row detected")

    print(file, "passed validation")