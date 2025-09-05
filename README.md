# Expense-tracker
#### Video Demo: (https://youtu.be/bevP6ik7MZM)
#### Description:

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



## app.py

`app.py` is the **main application file** for the expense tracker web app built using Flask. It serves as the entry point of the project and defines all the application logic, routing, and database interactions. The application utilizes sessions for user authentication and connects to an SQLite database called `expenses.db`.

- **Authentication and Sessions:** The app uses Flask-Session to manage user sessions, ensuring certain routes are only accessible when users are logged in. The `login_required` decorator, imported from `helpers.py`, restricts selected routes.
- **Routes:** The file defines routes for home, adding, deleting, and searching for expenses. It also provides routes for user login, logout, registration, and password change.
  - The `/` route shows the main dashboard with recent expenses, totals, and category-wise breakdowns.
  - `/add` and `/delete` allow adding and deleting expense entries, respectively.
  - `/search` allows filtering expenses by date range, showing a summary and category breakdown.
  - `/login`, `/logout`, `/register`, `/change` handle various authentication workflows.
- **Database Operations:** Interactions with the SQLite database include inserting new expenses, registering new users, validating credentials, and updating passwords.
- **Templates:** The routes render different HTML templates (e.g., `index.html`, `search.html`), passing all required data.

Overall, this file encapsulates the app’s logic and user workflow, managing HTTP requests and SQL queries.


## helpers.py

`helpers.py` contains a **utility function** to assist with authentication and route protection:

- **login_required Decorator:** This Python function, built using `functools.wraps`, checks if a user session contains a valid `"user_id"`. If not, it redirects the visitor to the login page. Otherwise, it executes the original (wrapped) function. This decorator is applied to all views in `app.py` that require authentication, securing sensitive areas of the application and abstracting away repeated logic for session validation.

This file helps keep the main application code clean and consistent when checking login status across multiple routes.


## requirements.txt

`requirements.txt` is a **dependency file** that lists all Python packages required to run the web app. When setting up the project, these packages are installed using pip, ensuring that all necessary modules are available.

- **Packages Listed:**
  - `cs50`: Used internally for certain helpers or database features.
  - `Flask`: The main micro web framework powering the app.
  - `Flask-Session`: For server-side session management.
  - `pytz`: Time zone support (may assist with date handling).
  - `requests`: For making HTTP requests (not heavily used in this code, but present for possible extensions).

This file is critical for portability and ensures the development environment can be reproduced exactly as needed.


## change.html

`change.html` is an **HTML template** for the "Change Password" feature, allowing users to modify their credentials.

- **Structure:**
  - Extends a base `layout.html` file, inheriting consistent styling and page layout.
  - Contains form fields for entering a new username, old password, new password, and password confirmation.
  - Designed to handle form submission for password changing and displays error messages if inputs are missing or don't match.
- **Role:** Presented to authenticated users who wish to update their username or password.

The template ensures a consistent and secure user interface for sensitive operations.


## login.html

`login.html` is an **HTML template** for the user login screen.

- **Structure:**
  - Also extends `layout.html` for uniform styling.
  - Offers form fields for username and password.
  - Displays relevant error messages for invalid or missing credentials.
- **Purpose:** Provides a simple, user-friendly interface to gain access to the application.

This template is crucial for managing access control and starting authenticated sessions.


## register.html

`register.html` is an **HTML template** for the user registration process.

- **Structure:**
  - Inherits from `layout.html`.
  - Contains fields for entering a new username, password, and confirmation of password.
  - Handles form submission and notifies users of errors such as missing details, mismatched passwords, or username conflicts.
- **Function:** Facilitates secure and easy onboarding of new users to the system.

Consistent with modern authentication UX, the file ensures users can seamlessly and securely join the platform.


## index.html

`index.html` is the **dashboard template** presented after login. While the file content isn’t shown, its function is inferred from `app.py`:

- **Features:**
  - Displays recent expense entries.
  - Shows total expenses, and a visualization or summary of spending by category.
  - Likely contains forms for adding and deleting expenses, as referenced in backend route handlers.

This core template houses the main interaction surface for users, providing real-time data and analytics.

## layout.html

`layout.html` is the **base template** that all other HTML files extend. While the content is not shown directly, its purpose is to maintain a consistent structure, including a header, styling links (including to `style.css`), and a standardized location for blocks of content filled by child templates. Such structure enforces code reuse and coherent UI experiences across the application.



## search.html

`search.html` is used to **display search results** when users filter expenses by a date range. Although file contents are not shown, this template is used by the `/search` route to render filtered expenses, summary totals, and category-wise breakdowns. It ensures quick user feedback when analyzing spending over customized timelines.
***

## style.css

`style.css` is the **stylesheet** controlling the visual appearance of the app.

- **Features:**
  - Defines fonts, color schemes, container layouts, paddings, margins, box shadows, border radii, etc.
  - Customizes forms, input fields (classes `.i`, `.b`), buttons, tables, and search widgets, ensuring they are readable and visually appealing.
  - Implements hover effects and transitions for a modern, interactive UX.


## How These Files Work Together

- Whenever a user visits the app, `app.py` handles the logic, relying on templates (like `index.html`, `change.html`, etc.) for rendering and `helpers.py` for authentication.
- All static and dynamic content appears uniformly styled due to the base layout and `style.css`.
- The database (`expenses.db`, not included here) is managed exclusively via the Python backend, keeping data secure and interactions efficient.
- The modular separation—between application logic, templates, helpers, and styles—ensures maintainability, scalability, and a solid user experience.
