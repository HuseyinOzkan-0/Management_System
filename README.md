# Management System

A comprehensive Python-based application for managing users, products, and activity logs. This system is designed to streamline administrative tasks and provide a central hub for data management from the command line.

## 🚀 Features

* **User Management:** Add, remove, and manage standard system users.
* **Admin Controls:** Separate administrative functions for role-based access.
* **Product Management:** Create, track, and organize product information.
* **Activity Logging:** Maintain a clear, persistent log of all significant actions within the system.

## 🏁 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.7+
* pip (Python package installer)

### 1. Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/HuseyinOzkan-0/Management_System.git](https://github.com/HuseyinOzkan-0/Management_System.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd Management_System
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Configuration

Before running the application, you must set up the required data files.

1.  Ensure you have a directory named `PMS/` inside the `Management_System` folder.
2.  Create the following empty files inside the `PMS/` directory:
    * `admins.txt`
    * `logs.txt`
    * `products.txt`
    * `users.txt`

The application will read from and write to these files to store all data.

### 3. Usage

To run the Management System, execute the following command from the root project directory:

```bash
python main.py