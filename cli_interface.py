def show_menu():
    print("Pharmaceutical Data Validation Software System")
    print("1. Download today's data")
    print("2. Download data by date")
    print("3. View error log")
    print("4. Exit")

while True:

    show_menu()

    choice = input("Select an option: ")

    if choice == "1":
        print("Downloading today's datasets...")

    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        print("Downloading datasets for", date)

    elif choice == "3":
        print("Displaying error log...")

    elif choice == "4":
        print("Exiting system")
        break

    else:
        print("Invalid option. Please try again.")