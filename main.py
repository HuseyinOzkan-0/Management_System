import functions
import os
os.makedirs("PMS", exist_ok=True)

while True:
    choice = functions.main_menu() #Main Menu
    if choice == "1":# User Login
        username = functions.user_login()
        if username:
            while True:
                print("\n--- User Panel ---")
                print("1. Logout to Main Menu")
                user_choice = input("Please choose an option: ")

                if user_choice == "1":
                    functions.add_logout_entry(username)
                    functions.quit_session(username)
                    break

    elif choice == "2": # Admin Login
        username = functions.admin_login()
        if username:
            while True:
                print("\n--- Admin Panel ---")
                print("1. List logs-reset logs")
                print("2. Logout to Main Menu")
                admin_choice = input("Please choose an option: ")

                if admin_choice == "1":
                    functions.list_and_reset_logs()
                if admin_choice == "2":
                    functions.add_logout_entry(username)
                    functions.quit_session(username)
                    break

    elif choice == "3": # Quit
        print("Quitting the program. Goodbye!")
        break

    else: # Invalid option
        print("Invalid option. Please try again.")