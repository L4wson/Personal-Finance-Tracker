import sqlite3

def create_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS income (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    source TEXT NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    category TEXT,
                    date TEXT,
                    description TEXT)''')
    conn.commit()
    conn.close()

def add_income(amount, source, date, description):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("INSERT INTO income (amount, source, date, description) VALUES (?, ?, ?, ?);", (amount, source, date, description))
    conn.commit()
    conn.close()

def add_expense(amount, category, date, description):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?);", (amount, category, date, description))
    conn.commit()
    conn.close()

def fetch_data(table):
    if table not in ['income', 'expenses']:
        raise ValueError("Invalid table name")
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    data = c.fetchall()
    conn.close()
    return data