import sqlite3

def create_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS income (...)''')
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (...)''')
    conn.commit()
    conn.close()

def add_income():
    pass

def add_expense():
    pass

def fetch_data():
    pass