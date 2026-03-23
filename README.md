# CSV Validator Project

This project was developed as part of the Unit 11 Advanced Programming assignment.

The system is designed to validate pharmaceutical CSV datasets before they are stored or used in research environments. It ensures that each file meets predefined structural and data integrity rules. Any errors detected during validation are recorded in an error log, allowing issues to be reviewed and corrected.

The application is implemented in Python and structured into multiple modules responsible for validation, logging, file tracking, and test data generation. A graphical user interface (GUI) built with Tkinter allows users to interact with the system easily.

The system simulates a file processing workflow by retrieving files from a simulated FTP server, validating their contents, and storing valid files in a structured archive organised by date.

## Key Features

- Downloading files from a simulated FTP server
- Detection of duplicate (already processed) files
- Validation of CSV file structure and data values
- Error logging with unique GUID identifiers
- Archiving valid files into date-based folders
- Search functionality to retrieve archived files by date

## Technologies Used

- Python
- Tkinter (GUI)
- File handling and validation logic
- Git and GitHub for version control

## Summary

The system demonstrates core software engineering principles, including data validation, process automation, and structured storage. It provides a simplified model of a real-world pharmaceutical data processing system, ensuring data quality and reliability.