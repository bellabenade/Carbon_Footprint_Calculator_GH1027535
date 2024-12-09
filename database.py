# sqlite3 installation: https://www.youtube.com/watch?v=XA3w8tQnYCA
# google copilot assistance with table creation
# how sqlite3 works: https://www.youtube.com/watch?v=girsuXz0yA8

import sqlite3


#connection to database and cursor
def connection_creation():
    connection = sqlite3.connect('company_clients.db')
    return connection

# Creation of tables
def user_table():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL)''')
    connection.commit()
    connection.close()

def carbon_table():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS carbon (
                        username TEXT,
                        electricity REAL,
                        nat_gas REAL,
                        fuel REAL,
                        waste_generated REAL,
                        waste_recycled REAL,
                        travel_km REAL,
                        fuel_efficiency REAL,
                        FOREIGN KEY(username) REFERENCES user_table(username))''')
    connection.commit()
    connection.close()

# functions to create, login and delete users
def add_user(username, password):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                   (username, password))
    connection.commit()
    connection.close()



def get_user(username):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    connection.close()
    return user

def delete_user(username):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    connection.commit()
    connection.close()

# function to insert entries in carbon table
def insert_info(username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO carbon (username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency))
    connection.commit()
    connection.close()

user_table()
carbon_table()

# def drop_table(table_name):
#     connection = connection_creation()
#     cursor = connection.cursor()
#     cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
#     connection.commit()
#     connection.close()
#
# drop_table('clients')

# Functions to display user and carbon table with saved entries
def fetch_all_entries(table_name):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    entries = cursor.fetchall()
    connection.close()
    return entries

def list_tables():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    connection.close()
    return tables

tables = list_tables()
print("Tables in the database:")
for table in tables:
    print(table[0])

for table in tables:
    print(f"\nEntries in table '{table[0]}':")
    entries = fetch_all_entries(table[0])
    for entry in entries:
        print(entry)

