# sqlite3 installation: https://www.youtube.com/watch?v=XA3w8tQnYCA
# google copilot assistance with table creation
# how sqlite3 works: https://www.youtube.com/watch?v=girsuXz0yA8

import sqlite3


#connection to database and cursor
def connection_creation():
    connection = sqlite3.connect('company_clients.db')
    return connection

def user_table():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL)''')
    connection.commit()
    connection.close()

def add_user(username, password):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
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
    connection.close()

user_table()
