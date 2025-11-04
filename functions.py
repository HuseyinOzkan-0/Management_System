import os
from datetime import datetime #To write log dates and times

#To print main menu and continue to next menu(Ayşenur)
def main_menu():
    print("\n----Main Menu----")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Quit")
    selection = input("Please select an option: ")
    return selection

#To login as a user and check for password and username(Ayşenur)
def user_login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    try:
        with open("PMS/users.txt", "r",encoding="utf8") as user:
            for line in user:
                parts=line.strip().split("-")
                if len(parts)==2:
                    correct_username, correct_password = parts
                    if username == correct_username and password == correct_password:
                        add_log_entry(username)
                        print(f"----Welcome {username} !----")
                        return username
        print("Incorrect username or password")
    except FileNotFoundError:
        print("Error: 'PMS/users.txt' file not found")

#To login as a admin and check for password and usernmae(Ayşenur)
def admin_login():
    username=input("Enter your username: ")
    password= input("Enter your password: ")
    try:
        with open("PMS/admins.txt", "r",encoding="utf8") as admin:
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
        print("Error: 'PMS/admins.txt' file not found")

#To quit seesion for both user and admin(Ayşenur)
def quit_session(username):
    if username:
        print(f"----{username} has logged out successfully.----")
    else:
        print("Quitting the program. Goodbye!")

#To add log entry when user or admin logs in(Kadir)
def add_log_entry(username):
    with open("PMS/logs.txt", "a", encoding="utf8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} logged in.\n")

#To add log entry when user or admin logs out(Kadir)
def add_logout_entry(username):
    with open("PMS/logs.txt", "a", encoding="utf8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} logged out.\n")

#To list logs and reset them as admin(Kadir)
def list_and_reset_logs():
    print("\n--- System Logs ---")
    try:
        with open("PMS/logs.txt", "r", encoding="utf8") as file:
            logs = file.readlines()
            if not logs:
                print("No log entries found.")
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("Log file not found.")
    
    reset_choice = input("Do you want to reset the logs? (y/n): ")
    if reset_choice.lower() == 'y':
        with open("PMS/logs.txt", "w", encoding="utf8") as file:
            file.write("")
        print("System logs have been reset.")
