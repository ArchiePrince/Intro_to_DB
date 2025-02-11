-- # Title:  CFull description
-- # Author: Archie Prince
-- # Filename: task_4.sql
-- # Date: 11.02.2025
-- # Objective: A script that prints the full description of the table books from the database alx_book_store in your MySQL server.

USE alx_book_store;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
