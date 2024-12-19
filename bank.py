import sqlite3
import decimal
import os
import bcrypt 

db = sqlite3.connect('bank.db')

print("Database Path:", os.path.abspath('bank.db'))

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance DECIMAL NOT NULL,
        password TEXT NOT NULL
    )
""")
db.commit()

def create_account():
    try:
        name = input("Enter your name: ")
        balance = float(input("Enter initial balance: "))
        password = input("Enter a password: ")

        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new account into the database
        insert_query = "INSERT INTO accounts (name, balance, password) VALUES (?, ?, ?)"
        values = (name, balance, hashed_password)
        cursor.execute(insert_query, values)
        db.commit()


        print("Account created successfully!")
    
        display_all_accounts()
        
    except sqlite3.Error as e:
        print("Error while creating account:", e)
        db.rollback()

def verify_password(account_id, password):
    select_query = "SELECT password FROM accounts WHERE id = ?"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        stored_hash = account[0]
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
    else:
        print("Account not found!")
        return False

def deposit():
    account_id = int(input("Enter account ID: "))
    password = input("Enter your password: ")

    if not verify_password(account_id, password):
        print("Incorrect password!")
        return
        
    amount = decimal.Decimal(input("Enter amount to deposit: "))
        
    amount = float(amount)

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
    password = input("Enter your password: ")
    
    if not verify_password(account_id, password):
        print("Incorrect password!")
        return

    amount = decimal.Decimal(input("Enter amount to withdraw: "))

    amount = float(amount)

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
        
def display_account():
    account_id = int(input("Enter account ID: "))
    password = input("Enter your password: ")

    if not verify_password(account_id, password):
        print("Incorrect password!")
        return

    select_query = "SELECT * FROM accounts WHERE id = ?"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        print("Account ID:", account[0])
        print("Name:", account[1])
        print("Balance:", account[2])
    else:
        print("Account not found!")
        
def display_all_accounts():
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    if accounts:
        print("\nAll Accounts:")
        for account in accounts:
            print(f"ID: {account[0]}, Name: {account[1]}")
    else:
        print("No accounts found.")
        
def delete_account():
    account_id = int(input("Enter account ID to delete: "))
    password = input("Enter your password to confirm deletion: ")

    # Verify the password before performing the operation
    if not verify_password(account_id, password):
        print("Incorrect password!")
        return

    # Check if the account exists
    select_query = "SELECT * FROM accounts WHERE id = ?"
    cursor.execute(select_query, (account_id,))
    account = cursor.fetchone()

    if account is not None:
        confirm = input(f"Are you sure you want to delete account ID {account_id} (y/n)? ")
        if confirm.lower() == 'y':
            delete_query = "DELETE FROM accounts WHERE id = ?"
            cursor.execute(delete_query, (account_id,))
            db.commit()

            print("Account deleted successfully!")
        else:
            print("Account deletion canceled.")
    else:
        print("Account not found!")
        
while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        display_account()
    elif choice == '5':
        display_all_accounts()
    elif choice == '6':
        delete_account()
    elif choice == '7':
        break
    else: 
        print("Invalid choice!")
        
db.close()