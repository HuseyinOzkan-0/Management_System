import os #To handle file paths and directories
from datetime import datetime #To write log dates and times

#To print main menu and continue to next menu
def main_menu():
    print("\n----Main Menu----" \
          "\n1. User Login" \
          "\n2. Admin Login" \
          "\n3. Quit")
    selection = input("Please select an option: ")
    return selection

#To login as a user and check for password and username
def user_login():
    username=input("Enter your username: ").lower()
    password=input("Enter your password: ")
    try:
        with open("MS/users.txt", "r",encoding="utf8") as user:
            for line in user:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_username, correct_password = parts
                    if username == correct_username and password == correct_password:
                        add_log_entry(username)
                        clear_terminal()
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'MS/users.txt' file not found")

#To login as a admin and check for password and usernmae
def admin_login():
    username=input("Enter your username: ").lower()
    password= input("Enter your password: ").lower()
    try:
        with open("MS/admins.txt", "r",encoding="utf8") as admin:
            for line in admin:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_admin_username, correct_admin_password = parts
                    if username == correct_admin_username and password == correct_admin_password:
                        add_log_entry(username)
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'MS/admins.txt' file not found")

#To quit seesion for both user and admin
def quit_session(username):
    if username:
        print(f"----{username} has logged out successfully.----")
    else:
        print("Quitting the program. Goodbye!")

#To add log entry when user or admin logs in
def add_log_entry(username):
    with open("MS/logs.txt", "a", encoding="utf8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} logged in.\n")

#To add log entry when user or admin logs out
def add_logout_entry(username):
    with open("MS/logs.txt", "a", encoding="utf8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} logged out.\n")

#To list logs and reset them as admin
def list_and_reset_logs(username):
    clear_terminal()
    print("\n--- System Logs ---")
    try:
        with open("MS/logs.txt", "r", encoding="utf8") as file:
            logs = file.readlines()
            if not logs:
                print("No log entries found.")
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("Log file not found.")
    
    reset_choice = input("\nDo you want to reset the logs? (y/n): ")
    if reset_choice.lower() == 'y':
        with open("MS/logs.txt", "w", encoding="utf8") as file:
            file.write("")
            file.write(f"Logs have been reseted by {username}.\n")
        print("System logs have been reset.")

#To add or remove products as user
def add_or_remove_product():
    product_name = input("Enter product name (alphabetic characters only): ").lower()

    if not product_name.isalpha():
        print("Error: Product name must contain only alphabetic characters.")
        return

    try:
        change = int(input("Enter a positive number to add stock, a negative number to remove: "))
    except ValueError:
        print("Error: Invalid number entered. Please enter a valid integer.")
        return

    products = {}
    try:
        with open("MS/products.txt", "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, quantity = line.split("-", 1)
                    products[name.strip()] = int(quantity.strip())
                except ValueError:
                    continue
    except FileNotFoundError:
        open("MS/products.txt", "w", encoding="utf8").close()

    current_stock = products.get(product_name, 0)
    new_stock = current_stock + change
    
    if product_name not in products and change <= 0:
        print("Product does not exist, cannot remove stock.")
        return
    if new_stock < 0:
        print(f"Not enough stock to remove. Current stock: {current_stock}")
        return
        
    products[product_name] = new_stock
    
    with open("MS/products.txt", "w", encoding="utf8") as file:
        for name, quantity in products.items():
            if quantity > 0:
                file.write(f"{name}-{quantity}\n")

    if change > 0:
        print(f"{change} units added to '{product_name}'. New stock: {new_stock}")
    elif change < 0:
        print(f"{abs(change)} units removed from '{product_name}'. New stock: {new_stock}")
    else:
        print("No change in stock was made.")

    if new_stock == 0:
        print(f"Stock for '{product_name}' is now zero and it has been removed from the list.")

#To list products as user
def list_products():
    clear_terminal()
    print("\n--- Product List ---")
    try:
        with open("MS/Products.txt", "r", encoding="utf8") as file:
            products = file.readlines()
            if not products:
                print("No products found.")
            for product in products:
                print(product.strip())
    except FileNotFoundError:
        print("No products have been added yet.")

#To clear terminal screen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#To add new users as admin
def add_new_user():
    username = input("Enter a new username (alphabetic characters only): ").lower()
    if not username.isalpha():
        print("Error: Username must contain only alphabetic characters.")
        return
        
    password = input("Enter a new password for the user (no punctuation): ")
    if any(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in password):
        print("Error: Password cannot contain punctuation marks.")
        return

    with open("MS/users.txt", "r", encoding="utf8") as file:
        for line in file:
            existing_username = line.strip().split("-")[0]
            if username == existing_username:
                clear_terminal()
                print(f"User '{username}' already exists. Please choose a different username.")
                return

    with open("MS/users.txt", "a", encoding="utf8") as file:
        file.write(f"{username}-{password}\n")
    print(f"User '{username}' was added successfully.")

#To list users as admin
def list_users():
    clear_terminal()
    print("\n--- User List ---")
    try:
        with open("MS/users.txt", "r", encoding="utf8") as file:
            users = file.readlines()
            if not users:
                print("No users found.")
            for user in users:
                print(user.strip().split('-')[0]) # Only show username
    except FileNotFoundError:
        print("No registered users found.")

#To remove users as admin
def remove_users():
    username_to_remove = input("Enter the username of the user to remove: ")
    try:
        with open("MS/users.txt", "r", encoding="utf8") as file:
            users = file.readlines()
        
        user_found = False
        with open("MS/users.txt", "w", encoding="utf8") as file:
            for user in users:
                if user.strip().split("-")[0] != username_to_remove:
                    file.write(user)
                else:
                    user_found = True
        
        if user_found:
            print(f"User '{username_to_remove}' was removed successfully.")
        else:
            print(f"User '{username_to_remove}' not found.") # Bug fix: f-string typo
    except FileNotFoundError:
        print("No registered users found.")

#To add new admins as admin
def add_new_admin():
    admin_name = input("Enter new admin username (alphabetic characters only): ").lower()
    if not admin_name.isalpha():
        print("Error: Admin username must contain only alphabetic characters.")
        return

    admin_password = input("Enter new admin password (no punctuation): ")
    if any(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in admin_password):
        print("Error: Password cannot contain punctuation marks.") 
        return

    # Check if admin already exists
    with open("MS/admins.txt", "r", encoding="utf8") as file:
        for line in file:
            existing_admin = line.strip().split("-")[0]
            if admin_name == existing_admin:
                print(f"Admin '{admin_name}' already exists. Please choose a different username.")
                return

    with open("MS/admins.txt", "a", encoding="utf8") as file:
        file.write(f"{admin_name}-{admin_password}\n")
    print(f"Admin '{admin_name}' added successfully.")

#To list admins as admin
def list_admins():
    print("\n--- Admin List ---")
    try:
        with open("MS/admins.txt", "r", encoding="utf8") as file:
            admins = file.readlines()
            if not admins:
                print("No admins found.")
            for admin in admins:
                print(admin.strip().split('-')[0]) # Only show admin name
    except FileNotFoundError:
        print("No registered admins found.")

#To remove admins as admin
def remove_admin():
    admin_to_remove = input("Enter the username of the admin to remove: ")
    try:
        with open("MS/admins.txt", "r", encoding="utf8") as file:
            admins = file.readlines()
            
        admin_found = False
        with open("MS/admins.txt", "w", encoding="utf8") as file:
            for admin in admins:
                if admin.strip().split("-")[0] != admin_to_remove:
                    file.write(admin)
                else:
                    admin_found = True
                    
        if admin_found:
            print(f"Admin '{admin_to_remove}' was removed successfully.")
        else:
            print(f"Admin '{admin_to_remove}' not found.")
    except FileNotFoundError:
        print("No registered admins found.")