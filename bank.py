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

def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))

    insert_query = "INSERT INTO accounts (name, balance) VALUES (?, ?)"
    values = (name, balance)
    cursor.execute(insert_query, values)
    db.commit()

    print("Account created successfully!")