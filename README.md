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
<img width="1857" height="657" alt="login" src="https://github.com/user-attachments/assets/e4abd6f0-4700-4489-9d39-bfe520c53a23" />

when you open the web application you will be send to login page.


<img width="1845" height="815" alt="register" src="https://github.com/user-attachments/assets/06bd4563-ea17-470c-9cf2-ec0f7bbadfa4" />

if you are first time user , you ahve to go to register page and then you can try to login
<img width="1832" height="906" alt="first page" src="https://github.com/user-attachments/assets/21706c42-deaf-4641-b86e-c18b34adbfc1" />

<img width="1816" height="668" alt="1" src="https://github.com/user-attachments/assets/4df4cf7e-1926-4e37-9f1d-e6671b05f744" />

<img width="805" height="857" alt="Screenshot 2025-09-05 192552" src="https://github.com/user-attachments/assets/6352c896-6730-4e84-9c20-cb15f89e1876" />

after login you will be send to expense tracker where you can add your expenses and get a pie chart for the expense based on categories.

<img width="753" height="431" alt="Screenshot 2025-09-05 192623" src="https://github.com/user-attachments/assets/a9209b95-b55b-49f9-ae63-8144f0b8f66b" />

you can search expense based on dates.

<img width="1847" height="732" alt="Screenshot 2025-09-05 192658" src="https://github.com/user-attachments/assets/7864d579-5694-4ceb-8b18-50025783ce85" />


you can change the password of your account.
