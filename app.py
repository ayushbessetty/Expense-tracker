from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_session import Session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os
from helpers import login_required


app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DATABASE = 'expenses.db'

# home route
@app.route('/')
@login_required
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expense WHERE id = ? ORDER BY date DESC LIMIT 10", (session["user_id"],))
        expenses = cursor.fetchall()
        # total expenses
        total = sum([row[1] for row in expenses])

        #spending by category
        cursor.execute("SELECT category, SUM(amount) FROM expense WHERE id=? GROUP BY category", (session["user_id"],))
        category_data = cursor.fetchall()

        categories = [row[0] for row in category_data]
        amounts = [row[1] for row in category_data]

    return render_template('index.html', expenses=expenses,total=total, categories=categories, amounts=amounts)

# add expense route
@app.route('/add', methods=['POST'])
@login_required
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    date = request.form['date']
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expense(id, category, amount, date) VALUES (?, ?, ?, ?)", (session["user_id"], category, amount, date,))
        print(session["user_id"])
    return redirect(url_for('index'))

# delete expense route
@app.route('/delete', methods=['POST'])
@login_required
def delete_expense():
    category = request.form.get('category')
    amount = request.form.get('amount')
    date = request.form.get('date')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expense WHERE category=? AND amount=? AND date=?', (category, amount, date))
    return redirect(url_for('index'))


# search by date range
@app.route('/search', methods=['GET'])
@login_required
def search():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expense WHERE date BETWEEN ? AND ? ORDER BY date DESC', (start_date, end_date))
        expenses = cursor.fetchall()
        total = sum([row[1] for row in expenses])


        #spending by category
        cursor.execute('SELECT category, SUM(amount) FROM expense WHERE date BETWEEN ? AND ? GROUP BY category', (start_date, end_date))
        category_data = cursor.fetchall()

        categories = [row[0] for row in category_data]
        amounts = [row[1] for row in category_data]
    return render_template('search.html', expenses=expenses, total=total, categories=categories, amounts=amounts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            return render_template('login.html', error="Please enter username.")

        password = request.form['password']
        if not password:
            return render_template('login.html', error="Please enter password.")
        
        # query database for username and password

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?",(username,))
            rows = cursor.fetchall()
        print(rows)
        if not rows or not check_password_hash(rows[0][2], password):
            return render_template('login.html', error="Invalid username or password.")
        # remember user session
        session["user_id"] = rows[0][0]

        return redirect('/')
    
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            return render_template('register.html', error="Please enter username.")

        password = request.form['password']
        if not password:
            return render_template('register.html', error="Please enter password.")
        
        confirmation = request.form['confirmation']
        if password != confirmation:
            return render_template('register.html', error="Passwords do not match.")

        # hash the password
        hashed_password = generate_password_hash(password)

        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, hashed_password))
                conn.commit()
        except sqlite3.IntegrityError:
            return render_template('register.html', error="Username already taken.")

        return redirect('/login')
    
    return render_template('register.html')


@app.route('/change', methods=['GET', 'POST'])
@login_required
def change():
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            return render_template('change.html', error="Please enter username.")

        opassword = request.form['old_password']
        if not opassword:
            return render_template('change.html', error="Please enter password.")
        
        npassword = request.form['new_password']
        if not npassword:
            return render_template('change.html', error="Please enter password.")
        
        confirmation = request.form['confirmation']
        if npassword != confirmation:
            return render_template('change.html', error="Passwords do not match.")

        # hash the password
        hashed_password = generate_password_hash(npassword)

        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET username=?, password=? WHERE id=?", (username, hashed_password, session["user_id"]))
                conn.commit()
        except sqlite3.IntegrityError:
            return render_template('change.html', error="Username already taken.")

        return redirect('/login')
    
    return render_template('change.html')














if __name__ == '__main__':
    app.run(debug=True)

