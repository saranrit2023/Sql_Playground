from flask import Blueprint, render_template, request, flash
from app.db import get_db, init_db
import datetime
import json

main = Blueprint('main', __name__)

# 🔴 VULNERABLE LOGIN PAGE
@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ❌ Vulnerable raw SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return f"Welcome {result[1]}!"
            else:
                flash("Login failed")
        except Exception as e:
            log_entry = {
                "time": str(datetime.datetime.now()),
                "error": str(e),
                "input": {"username": username, "password": password}
            }
            with open("logs/sqli_logs.txt", "a") as log:
                log.write(json.dumps(log_entry) + "\n")
            flash("SQL Error detected")
    return render_template("login.html")


# ✅ SAFE LOGIN PAGE USING PARAMETERIZED QUERY
@main.route('/safe', methods=['GET', 'POST'])
def safe_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()

        # ✅ Safe parameterized query
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        if result:
            return f"[SAFE] Welcome {result[1]}!"
        else:
            flash("[SAFE] Login failed")

    return render_template("login.html")


# 🔁 RESET DATABASE
@main.route('/init')
def reset_db():
    init_db()
    return "✅ Database reset successfully. <a href='/'>Go to Login</a>"


# 📄 VIEW SQL INJECTION LOGS
@main.route('/logs')
def view_logs():
    try:
        with open("logs/sqli_logs.txt", "r") as f:
            logs = f.read().replace("\n", "<br>")
        return f"<h3>SQLi Log Output</h3><div style='background:#f0f0f0;padding:10px'>{logs}</div>"
    except FileNotFoundError:
        return "No logs found."
