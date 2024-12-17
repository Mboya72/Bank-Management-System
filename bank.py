import sqlite3
import decimal

db = sqlite3.connect('bank.db')

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance DECIMAL NOT NULL
    )
""")
db.commit()