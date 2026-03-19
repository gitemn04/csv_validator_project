import csv
import random
from datetime import datetime


# ✅ CORRECT headers (must match validator)
headers = ["batch", "timestamp", "value"]


def generate_valid_csv(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        for i in range(10):
            value = round(random.uniform(0, 9.9), 2)
            writer.writerow([
                i + 1,
                datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                value
            ])


def generate_invalid_csv(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        # ❌ invalid value (string instead of number)
        writer.writerow([
            1,
            datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "abc"
        ])


# filenames already correct
generate_valid_csv("MED_DATA_001.csv")
generate_invalid_csv("MED_DATA_002.csv")

print("CSV files generated.")