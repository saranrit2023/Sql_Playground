import sqlite3

def get_db():
    conn = sqlite3.connect("users.db")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )''')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'pass1')")
    conn.commit()
    conn.close()
