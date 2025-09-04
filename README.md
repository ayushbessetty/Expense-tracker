# Expense-tracker
This project is a Flask-based expense tracker web application that allows users to securely register, log in, and manage their personal expenses. It provides features to add, delete, and view expenses, see recent spending, search by date range, and visualize spending by category.

User Authentication: Secure login, registration, logout, and password change flows using hashed passwords and session management.

Expense Management: Users can add, remove, and view recent expenses, with each expense categorized and timestamped.

Search and Analytics: Users can filter expenses by date range and view summarized spending by category for easy analysis.

Simple Storage: Uses a local SQLite database (expenses.db) for data storage.

Web Interface: Clean web pages for login, registration, dashboard, and search results using Flask templates

Technical Stack

Backend: Flask framework with Flask-Session for session management.

Database: SQLite for storing user credentials and expenses.

Security: Passwords are securely hashed using Werkzeug utilities.

Dependencies: Relies on Flask, Flask-Session, cs50, requests, and pytz libraries
