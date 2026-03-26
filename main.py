import tkinter as tk
from tkinter import scrolledtext
import os
import shutil
from datetime import date

from validator import *
from logger import Logger
from csv_generator import generate_valid_csv, generate_invalid_csv
from file_tracker import is_processed, mark_as_processed

logger = Logger()

# -------------------------
# FUNCTIONS
# -------------------------

def generate_files():
    output_box.insert(tk.END, "Generating CSV files...\n")

    generate_valid_csv("MED_DATA_001.csv")
    generate_invalid_csv("MED_DATA_002.csv")

    output_box.insert(tk.END, "CSV files generated successfully.\n\n")
    update_file_list()


def save_to_archive(filename):
    today = str(date.today())
    folder = f"archive/{today}"

    if not os.path.exists(folder):
        os.makedirs(folder)

    destination = os.path.join(folder, filename)

    try:
        shutil.copy(filename, destination)
        output_box.insert(tk.END, f"{filename} archived successfully\n", "success")

        try:
            os.remove(filename)
        except:
            pass

    except Exception as e:
        output_box.insert(tk.END, f"Archive error: {e}\n")


def validate_files():
    files = ["MED_DATA_001.csv", "MED_DATA_002.csv"]

    for file in files:
        output_box.insert(tk.END, f"Checking file: {file}\n")

        if is_processed(file):
            output_box.insert(tk.END, f"{file} already processed\n\n")
            continue

        if not validate_filename(file):
            logger.log_error(f"{file} -> Invalid filename")
            output_box.insert(tk.END, f"{file} Invalid filename\n")
            continue

        if not validate_empty_file(file):
            logger.log_error(f"{file} -> File is empty")
            output_box.insert(tk.END, f"{file} File is empty\n")
            continue

        with open(file, "r") as f:
            header = f.readline()

            if not validate_headers(header):
                logger.log_error(f"{file} -> Invalid headers")
                output_box.insert(tk.END, f"{file} Invalid headers\n")
                continue

            valid = True

            for row in f:
                if not validate_row(row):
                    logger.log_error(f"{file} -> Invalid row detected")
                    output_box.insert(tk.END, f"{file} Invalid row detected\n")
                    valid = False

            if valid:
                output_box.insert(tk.END, f"{file} passed validation\n", "success")
                mark_as_processed(file)
                save_to_archive(file)

        output_box.insert(tk.END, "\n")


# NEW FEATURE: DATE SEARCH
def search_by_date():
    selected_date = date_entry.get()

    folder = f"archive/{selected_date}"

    output_box.insert(tk.END, f"\nSearching archive for: {selected_date}\n")

    if os.path.exists(folder):
        files = os.listdir(folder)

        if files:
            for f in files:
                output_box.insert(tk.END, f"Found: {f}\n", "success")
        else:
            output_box.insert(tk.END, "No files found in this date\n")
    else:
        output_box.insert(tk.END, "No archive folder for this date\n")


def update_file_list():
    file_listbox.delete(0, tk.END)

    for file in os.listdir():
        if file.endswith(".csv") or file.endswith(".txt"):
            file_listbox.insert(tk.END, file)


def open_file():
    selected = file_listbox.get(tk.ACTIVE)
    if selected:
        os.startfile(selected)


def view_log():
    if os.path.exists("error_log.txt"):
        with open("error_log.txt", "r") as f:
            content = f.read()
            output_box.insert(tk.END, "\n--- ERROR LOG ---\n")
            output_box.insert(tk.END, content + "\n")
    else:
        output_box.insert(tk.END, "No log file found\n")


def clear_output():
    output_box.delete(1.0, tk.END)

def download_from_ftp():
    ftp_folder = "ftp_server"

    output_box.insert(tk.END, "Connecting to FTP server...\n")

    if not os.path.exists(ftp_folder):
        output_box.insert(tk.END, "FTP folder not found\n")
        return

    files = os.listdir(ftp_folder)

    if not files:
        output_box.insert(tk.END, "No files on FTP server\n")
        return

    for file in files:

        if not file.endswith(".csv"):
            continue

        if is_processed(file):
            output_box.insert(tk.END, f"Skipped (already processed): {file}\n")
            continue

        source = os.path.join(ftp_folder, file)
        destination = file

        shutil.copy(source, destination)
        output_box.insert(tk.END, f"Downloaded: {file}\n", "success")

    output_box.insert(tk.END, "FTP download complete\n\n")
    update_file_list()

# -------------------------
# HOVER EFFECT
# -------------------------

def on_enter(e):
    e.widget['background'] = '#00adb5'

def on_leave(e):
    e.widget['background'] = '#393e46'


# -------------------------
# GUI SETUP
# -------------------------

root = tk.Tk()
root.title("Pharmaceutical CSV Validation System")
root.geometry("800x550")
root.configure(bg="#222831")

# TITLE
title = tk.Label(
    root,
    text="Pharmaceutical CSV Validator",
    font=("Arial", 20, "bold"),
    bg="#222831",
    fg="#00adb5"
)
title.pack(pady=10)

#  DATE INPUT (AUTO FILLED WITH TODAY)
date_entry = tk.Entry(root, font=("Arial", 10))
date_entry.pack(pady=5)
date_entry.insert(0, str(date.today()))

# BUTTON FRAME
btn_frame = tk.Frame(root, bg="#222831")
btn_frame.pack()


def create_button(text, command):
    btn = tk.Button(
        btn_frame,
        text=text,
        command=command,
        bg="#393e46",
        fg="white",
        font=("Arial", 11, "bold"),
        width=22,
        relief="flat"
    )
    btn.pack(pady=5)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn


# BUTTONS
create_button("Generate CSV Files", generate_files)
create_button("Download from FTP", download_from_ftp)   #
create_button("Validate Files", validate_files)
create_button("Search by Date", search_by_date)
create_button("Open Selected File", open_file)
create_button("View Error Log", view_log)
create_button("Refresh File List", update_file_list)
create_button("Clear Output", clear_output)
# MAIN FRAME
main_frame = tk.Frame(root, bg="#222831")
main_frame.pack(pady=10)

# FILE LIST
file_listbox = tk.Listbox(
    main_frame,
    width=30,
    height=18,
    bg="#393e46",
    fg="white",
    font=("Arial", 10)
)
file_listbox.grid(row=0, column=0, padx=10)

# OUTPUT BOX
output_box = scrolledtext.ScrolledText(
    main_frame,
    width=55,
    height=18,
    bg="#393e46",
    fg="white",
    font=("Arial", 10)
)
output_box.grid(row=0, column=1, padx=10)

# SUCCESS COLOR
output_box.tag_config("success", foreground="lightgreen")

# INITIAL LOAD
update_file_list()

# RUN
root.mainloop()