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
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
                        username TEXT,
                        electricity REAL,
                        nat_gas REAL,
                        fuel REAL,
                        energy REAL,
                        waste_generated REAL,
                        waste_recycled REAL,
                        waste REAL,
                        travel_km REAL,
                        fuel_efficiency REAL,
                        travel REAL,
                        carbon_footprint REAL,
                        FOREIGN KEY(username) REFERENCES users(username)''')
    connection.commit()
    connection.close()


# functions to create entries
def add_user(username, password):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    connection.commit()
    connection.close()

#def add_info():


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
    connection.close()

user_table()
