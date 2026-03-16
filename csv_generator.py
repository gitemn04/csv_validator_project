import csv
import random
from datetime import datetime


headers = [
    "batch_id",
    "timestamp",
    "reading1",
    "reading2",
    "reading3",
    "reading4",
    "reading5",
    "reading6",
    "reading7",
    "reading8",
    "reading9",
    "reading10"
]


def generate_valid_csv(filename):

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        for i in range(10):

            readings = [round(random.uniform(0, 9.9), 3) for _ in range(10)]

            writer.writerow(
                [i + 1, datetime.now().strftime("%H:%M:%S")] + readings
            )


def generate_invalid_csv(filename):

    with open(filename, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(headers)

        readings = [round(random.uniform(0, 9.9), 3) for _ in range(9)]

        readings.append(10.5)

        writer.writerow([1, datetime.now().strftime("%H:%M:%S")] + readings)


generate_valid_csv("valid_pharma_data.csv")
generate_invalid_csv("invalid_pharma_data.csv")

print("CSV files generated.")