# <span style="color:#CC1512;"> Bank Management System</span>
## Overview
This is a simple command-line Bank Management System implemented using Python and SQLite. 

The system allows users to create bank accounts, deposit money, withdraw money, and display account details. 

The balances are stored using the DECIMAL data type for better accuracy with financial operations.

## Features
**Create Account:** Allows users to create a new account with a specified name and initial balance.

**Deposit:** Allows users to deposit a specified amount into an existing account.

**Withdraw:** Allows users to withdraw a specified amount from an existing account if sufficient funds are available.

**Display Account:** Displays the details of an account (ID, name, and balance) based on the account ID.

## Technologies used
1.python 3.12

2.SQLite

## Installation
Ensure you have Python 3.x installed on your machine.

The sqlite3 library is included in Python's standard library, so no additional installation is required.

Clone or download this repository to your local machine.

## Database
The system uses an SQLite database called bank.db to store account information. The database contains a single table, accounts, which has the following columns:
```
id (INTEGER, PRIMARY KEY AUTOINCREMENT): The unique identifier for each account.
name (TEXT, NOT NULL): The name of the account holder.
balance (DECIMAL, NOT NULL): The current balance of the account.
```
## Usage
```
1. Create Account
To create a new account:

The user is prompted to enter their name.
The user is prompted to enter the initial balance of the account.
After successful creation, a confirmation message is displayed.
2. Deposit
To deposit money into an account:

The user is prompted to enter the account ID.
The user is prompted to enter the amount to deposit.
If the account exists, the balance is updated accordingly, and a success message is displayed.
If the account does not exist, an error message is displayed.
3. Withdraw
To withdraw money from an account:

The user is prompted to enter the account ID.
The user is prompted to enter the amount to withdraw.
If the account exists and there are sufficient funds, the balance is updated, and a success message is displayed.
If the account does not exist or if there are insufficient funds, an error message is displayed.
4. Display Account
To display account information:

The user is prompted to enter the account ID.
If the account exists, the account's ID, name, and balance are displayed.
If the account does not exist, an error message is displayed.
5. Exit
The user can exit the program by choosing option 5 from the main menu.
```

## Example Usage
```
bash
Copy code
Bank Management System
1. Create Account
2. Deposit
3. Withdraw
4. Display Account
5. Exit

Enter your choice: 1
Enter your name: John Doe
Enter initial balance: 1000
Account created successfully!

Bank Management System
1. Create Account
2. Deposit
3. Withdraw
4. Display Account
5. Exit

Enter your choice: 2
Enter account ID: 1
Enter amount to deposit: 500
Deposit successful!

Bank Management System
1. Create Account
2. Deposit
3. Withdraw
4. Display Account
5. Exit

Enter your choice: 3
Enter account ID: 1
Enter amount to withdraw: 200
Withdrawal successful!

Bank Management System
1. Create Account
2. Deposit
3. Withdraw
4. Display Account
5. Exit

Enter your choice: 4
Enter account ID: 1
Account ID: 1
Name: John Doe
Balance: 1300
```

## License

