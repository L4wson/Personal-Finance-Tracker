import sqlite3

def create_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS income (...)''')
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (...)''')
    conn.commit()
    conn.close()

def add_income():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("INSERT INTO income (amount, source, date, description) VALUES (?, ?, ?, ?);", (amount, source, date, description))
    conn.commit()
    conn.close()

def add_expense():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("INSERT INTO expense (amount, category, date, description) VALUES (?, ?, ?, ?);", (amount, category, date, description))
    conn.commit()
    conn.close()

def fetch_data():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    data = c.fetchall()
    conn.close()
    return data