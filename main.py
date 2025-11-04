import functions #Importing functions module
import os #To handle file paths and directories
os.makedirs("MS", exist_ok=True) #Check MS directory exists

while True:
    choice = functions.main_menu() #Main Menu
    if choice == "1":# User Login
        username = functions.user_login()
        if username:# User logged in successfully
            while True:# User Panel
                print("""
--- User Panel ---
1. Add or Remove Product Stock
2. List Products
3. Clear Terminal
4. Logout to Main Menu""")
                user_choice = input("Please choose an option: ")
                if user_choice == "1":#add or remove product stock
                    functions.add_or_remove_product()
                elif user_choice == "2":#list products
                    functions.list_products()
                elif user_choice == "3":#clear terminal
                    functions.clear_terminal()
                elif user_choice == "4":# Logout to Main Menu
                    functions.clear_terminal()
                    functions.add_logout_entry(username)
                    functions.quit_session(username)
                    break
    elif choice == "2": # Admin Login
        username = functions.admin_login()
        if username:# Admin logged in successfully
            while True:# Admin Panel
                print("""
--- Admin Panel ---
1. Log List and Reset
2. Add New User
3. List Users
4. remove User
5. Add New Admin
6. List Admins
7. Remove Admin
8. Clear Terminal
9. Logout to Main Menu""")
                admin_choice = input("Please choose an option: ")
                if admin_choice == "1":#Log list and reset
                    functions.list_and_reset_logs(username)
                elif admin_choice == "2":#To add new user as admin
                    functions.add_new_user
                elif admin_choice == "3":#To list users as admin
                    functions.list_users()
                elif admin_choice == "4":#To remove user as admin
                    functions.list_users()
                    functions.remove_users()
                elif admin_choice == "5":#To add new admin as admin
                    functions.add_new_admin()
                elif admin_choice == "6":#To list admins as admin
                    functions.list_admins()
                elif admin_choice == "7":#To remove admin as admin
                    functions.list_admins()
                    functions.remove_admin()
                elif admin_choice == "8":# Clear terminal
                    functions.clear_terminal()
                elif admin_choice == "9":# Logout to Main Menu
                    functions.add_logout_entry(username)
                    functions.quit_session(username)
                    break
    elif choice == "3": # Quit
        functions.clear_terminal()
        print("Quitting the program. Goodbye!")
        break
    else: # Invalid option
        print("Invalid option. Please try again.")