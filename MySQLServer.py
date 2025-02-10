# Title:  Let's Build Your Database: Your Gateway to Data Adventure!
# Author: Archie Prince
# Filename: MySQLServer.py
# Date: 10.02.2025
# Objective: A simple python script that creates the database alx_book_store in your MySQL server.

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='user_name',  # Replace with your MySQL username
            password='user_password!'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()