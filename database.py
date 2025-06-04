import mysql.connector
from mysql.connector import Error

# === Utility Functions ===

def get_connection():
    try:
        return mysql.connector.connect(
            user='root',
            password='1234',
            host='localhost',
            database='passwords_manager'
        )
    except Error as err:
        print(f"Connection Error: {err}")
        return None


def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234'
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS passwords_manager")
        print("Database created successfully")
        connection.close()
    except Error as err:
        print(f"Database Creation Error: {err}")


def execute_query(connection, query):
    if connection is None:
        print("Error: No connection to database")
        return

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Query Error: {err}")


def add_column_if_not_exists(cursor, table, column, definition):
    query = f"""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table}' AND COLUMN_NAME = '{column}'
    """
    cursor.execute(query)
    if cursor.fetchone()[0] == 0:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
        print(f"Added column '{column}' to '{table}'.")


# === Setup ===

# Step 1: Create database if it doesn't exist
create_database()

# Step 2: Connect to the newly created database
conn = get_connection()

# Step 3: Define and create tables
table_queries = [
    """
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(100) PRIMARY KEY UNIQUE NOT NULL,
        email VARCHAR(100),
        password VARCHAR(100) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100),
        site VARCHAR(100) NOT NULL,
        url VARCHAR(100),
        acc_username VARCHAR(100),
        acc_password VARCHAR(100) NOT NULL,
        dateModified DATE,
        FOREIGN KEY (username) REFERENCES users(username)
    )
    """
]

for query in table_queries:
    execute_query(conn, query)