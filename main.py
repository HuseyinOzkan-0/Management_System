import functions  # Importing functions module
import os         # To handle file paths and directories

def handle_user_panel(username):
    user_actions = {
        "1": functions.add_or_remove_product,
        "2": functions.list_products,
        "3": functions.clear_terminal,
    }
    while True:
        print("""
--- User Panel ---
1. Add or Remove Product Stock
2. List Products
3. Clear Terminal
4. Logout to Main Menu""")
        choice = input("Please choose an option: ")
        if choice in user_actions:
            user_actions[choice]()
        elif choice == "4":
            functions.clear_terminal()
            functions.add_logout_entry(username)
            functions.quit_session(username)
            print(f"Logging out {username}...")
            break  # Exit the user panel loop
        else:
            print("Invalid option. Please try again.")

def handle_admin_panel(username):
    admin_actions = {
        "2": functions.add_new_user,    
        "3": functions.list_users,
        "5": functions.add_new_admin,   
        "6": functions.list_admins,
        "8": functions.clear_terminal,
    }
    while True:
        print("""
--- Admin Panel ---
1. Log List and Reset
2. Add New User
3. List Users
4. Remove User
5. Add New Admin
6. List Admins
7. Remove Admin
8. Clear Terminal
9. Logout to Main Menu""")
        admin_choice = input("Please choose an option: ")
        if admin_choice in admin_actions:
            admin_actions[admin_choice]()
        elif admin_choice == "1":
            functions.list_and_reset_logs(username)
        elif admin_choice == "4":
            functions.list_users()      
            functions.remove_users()
        elif admin_choice == "7":
            functions.list_admins()     
            functions.remove_admin()
        elif admin_choice == "9":
            functions.clear_terminal()
            functions.add_logout_entry(username)
            functions.quit_session(username)
            print(f"Logging out {username}...")
            break  # Exit the admin panel loop
        else:
            print("Invalid option. Please try again.")

def main():
    os.makedirs("MS", exist_ok=True)
    while True:
        choice = functions.main_menu()
        if choice == "1":  # User Login
            username = functions.user_login()
            if username:  # User logged in successfully
                handle_user_panel(username)  # <-- Cleaner!
        elif choice == "2":  # Admin Login
            username = functions.admin_login()
            if username:  # Admin logged in successfully
                handle_admin_panel(username)  # <-- Cleaner!
        elif choice == "3":  # Quit
            functions.clear_terminal()
            print("Quitting the program. Goodbye!")
            break  # Exit the main application loop
        else:  # Invalid option
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()