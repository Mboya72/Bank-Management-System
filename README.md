# Bank Management System
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
