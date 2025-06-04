# 🔐 Passwords Manager

A desktop application built with Python's Tkinter for GUI and MySQL for secure storage of user credentials. This Passwords Manager allows users to create accounts, log in, and securely store and manage their passwords.

## 🚀 Features

* User account creation and authentication
* Secure storage of passwords
* User-friendly graphical interface

## 🛠️ Technologies Used

* **Programming Language:** Python
* **GUI Library:** Tkinter
* **Database:** MySQL
* **Libraries:** `mysql-connector-python , tkinter`([github.com][1])

## 📁 Project Structure

The project consists of the following files:

* `appscreen.py`: Main application interface.
* `createAccount.py`: Handles user account creation.
* `database.py`: Manages database connections and queries.
* `insertData.py`: Handles insertion of user data into the database.
* `login.py`: Manages user login functionality.
* `README.md`: Project documentation.([github.com][1])

## 🔧 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Saiff-Tunio/Passwords-Manager.git
   cd Passwords-Manager
   ```



2. **Install required libraries:**

   ```bash
   pip install mysql-connector-python
   pip install tkinter
   ```



3. **Set up the MySQL database:**

   * Ensure MySQL is installed and running.
   * Update the database connection details in `database.py` accordingly.

4. **Run the application:**

   ```bash
   python appscreen.py
   ```


## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

