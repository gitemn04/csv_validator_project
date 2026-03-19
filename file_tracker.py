import os

TRACKER_FILE = "processed_files.txt"


def load_processed_files():
    if not os.path.exists(TRACKER_FILE):
        return set()

    with open(TRACKER_FILE, "r") as file:
        return set(line.strip() for line in file if line.strip())


def is_processed(filename):
    processed_files = load_processed_files()
    return filename in processed_files


def mark_as_processed(filename):
    with open(TRACKER_FILE, "a") as file:
        file.write(filename + "\n")