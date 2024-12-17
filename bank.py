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
    
def deposit():
    account_id = int(input("Enter account ID: "))
    amount = decimal.Decimal(input("Enter amount to deposit: "))

    select_query = "SELECT * FROM accounts WHERE id = ?"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        new_balance = account[2] + amount
        update_query = "UPDATE accounts SET balance = ? WHERE id = ?"
        cursor.execute(update_query, (new_balance, account_id))
        db.commit()

        print("Deposit successful!")
    else:
        print("Account not found!")
        
def withdraw():
    account_id = int(input("Enter account ID: "))
    amount = decimal.Decimal(input("Enter amount to withdraw: "))

    select_query = "SELECT * FROM accounts WHERE id = ?"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        if account[2] >= amount:
            new_balance = account[2] - amount
            update_query = "UPDATE accounts SET balance = ? WHERE id = ?"
            cursor.execute(update_query, (new_balance, account_id))
            db.commit()

            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")
    else:
        print("Account not found!")