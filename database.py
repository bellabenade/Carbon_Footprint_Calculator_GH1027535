# sqlite3 installation: https://www.youtube.com/watch?v=XA3w8tQnYCA
# how sqlite3 works: https://www.youtube.com/watch?v=girsuXz0yA8

import sqlite3
import plotly.express as pe
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

#connection to database and cursor
def connection_creation():
    connection = sqlite3.connect('company_clients.db')
    return connection

# Creation of tables
def user_table():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT UNIQUE PRIMARY KEY,
                        password TEXT NOT NULL)''')
    connection.commit()
    connection.close()

def carbon_table():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS carbon (
                        username TEXT NOT NULL,
                        electricity DECIMAL(10, 2) NOT NULL,
                        nat_gas DECIMAL(10, 2) NOT NULL,
                        fuel DECIMAL(10, 2) NOT NULL,
                        waste_generated DECIMAL(10, 2) NOT NULL,
                        waste_recycled INTEGER,
                        travel_km DECIMAL(10, 2) NOT NULL,
                        fuel_efficiency DECIMAL(10, 2) NOT NULL,
                        cur_date DATE NOT NULL,
                        FOREIGN KEY(username) REFERENCES user_table(username))''')
    connection.commit()
    connection.close()

def calculated():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS calculated (
                        username TEXT NOT NULL,
                        cur_date DATE NOT NULL,
                        energy DECIMAL(10, 2) NOT NULL,
                        waste DECIMAL(10, 2) NOT NULL,
                        travel DECIMAL(10, 2) NOT NULL,
                        carbon_footprint INTEGER NOT NULL,
                        PRIMARY KEY (username, cur_date)
                        UNIQUE (username, cur_date) ON CONFLICT REPLACE
                        FOREIGN KEY (username) REFERENCES users(cur_date))''')
    connection.commit()
    connection.close()

# functions to change tables:
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

def insert_info(username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, cur_date):
    #username will also have to be checked
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''SELECT * 
    FROM carbon 
    WHERE username = ? AND cur_date = ?''',
                   (username, cur_date))
    exist = cursor.fetchone()

    if exist:
        cursor.execute('''UPDATE carbon
        SET electricity = ?, nat_gas = ?, fuel = ?, waste_generated = ?, waste_recycled = ?, travel_km = ?, fuel_efficiency = ?
        WHERE username = ? AND cur_date = ?''', (electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, username, cur_date))
    else:
        cursor.execute('INSERT INTO carbon VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km,
                        fuel_efficiency, cur_date))
    connection.commit()
    connection.close()
    calculate_values()

def calculate_values():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute('''SELECT username, cur_date, 
                        printf("%.2f",electricity * 12 * 0.0005 + nat_gas * 12 * 0.0053 + fuel * 12 * 2.32) AS energy, 
                        printf("%.2f",waste_generated * 12 * (0.57 - (waste_recycled)/100)) AS waste, 
                        printf("%.2f",travel_km * (1.0 / fuel_efficiency) * 2.31) AS travel
                        FROM carbon''')
    result = cursor.fetchall()

    for i in result:
        username, cur_date, energy, waste, travel = i
        carbon_footprint = int(float(energy) + float(waste) + float(travel))
        cursor.execute('''INSERT OR REPLACE INTO calculated (username, cur_date, energy, waste, travel, carbon_footprint)
                            VALUES (?, ?, ?, ?, ?, ?)''', (username, cur_date, energy, waste, travel, carbon_footprint))
    connection.commit()
    connection.close()

user_table()
carbon_table()
calculated()
calculate_values()

def herpa_derpa():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT carbon_footprint 
                    FROM calculated 
                    WHERE username = '{st.session_state.username}' 
                    ORDER BY cur_date DESC
                    LIMIT 1''')
    carbon_foot = cursor.fetchone()[0]
    connection.close()
    return carbon_foot

def pie_chart():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT energy, waste, travel
                    FROM calculated
                    WHERE username = '{st.session_state.username}'
                    ORDER BY cur_date DESC
                    LIMIT 1''')
    values1 = cursor.fetchall()
    connection.close()

    val1_table = pd.DataFrame(values1, columns= ['energy', 'waste', 'travel'])
    val1_table_values = val1_table[['energy', 'waste', 'travel']].sum()

    pie = pe.pie(
        names = ['Energy', 'Waste', 'Travel'],
        values = [val1_table_values['energy'], val1_table_values['waste'], val1_table_values['travel']],
        title = 'My consumption this month:')

    st.plotly_chart(pie)

def energy_bar_chart():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT cur_date, energy
                    FROM calculated
                    WHERE username = '{st.session_state.username}'
                    ORDER BY cur_date DESC
                    LIMIT 12''')
    values2 = cursor.fetchall()
    connection.close()

    val2_table = pd.DataFrame(values2, columns=['cur_date', 'energy'])

    bar2 = go.Bar(x = val2_table['cur_date'], y = val2_table['energy'], name = 'Energy Consumption')
    line2 = go.Scatter(x = val2_table['cur_date'], y = val2_table['energy'], mode = 'lines+markers', name = 'Trend')

    trend2 = go.Figure()
    trend2.add_trace(bar2)
    trend2.add_trace(line2)

    trend2.update_layout(title = 'Energy Consumption Over The Last Year',
                        xaxis_title = 'Date',
                        yaxis_title = 'Energy Consumption')

    st.plotly_chart(trend2)

def waste_bar_chart():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT cur_date, waste
                    FROM calculated
                    WHERE username = '{st.session_state.username}'
                    ORDER BY cur_date DESC
                    LIMIT 12''')
    values3 = cursor.fetchall()
    connection.close()

    val3_table = pd.DataFrame(values3, columns=['cur_date', 'waste'])

    bar3 = go.Bar(x = val3_table['cur_date'], y = val3_table['waste'], name = 'Waste Management')
    line3 = go.Scatter(x = val3_table['cur_date'], y = val3_table['waste'], mode = 'lines+markers', name = 'Trend')

    trend3 = go.Figure()
    trend3.add_trace(bar3)
    trend3.add_trace(line3)

    trend3.update_layout(title = 'Travel Over The Last Year',
                        xaxis_title = 'Date',
                        yaxis_title = 'Energy Consumption')

    st.plotly_chart(trend3)

def travel_bar_chart():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT cur_date, travel
                    FROM calculated
                    WHERE username = '{st.session_state.username}'
                    ORDER BY cur_date DESC
                    LIMIT 12''')
    values4 = cursor.fetchall()
    connection.close()

    val4_table = pd.DataFrame(values4, columns=['cur_date', 'travel'])

    bar4 = go.Bar(x = val4_table['cur_date'], y = val4_table['travel'], name = 'Travel')
    line4 = go.Scatter(x = val4_table['cur_date'], y = val4_table['travel'], mode = 'lines+markers', name = 'Trend')

    trend4 = go.Figure()
    trend4.add_trace(bar4)
    trend4.add_trace(line4)

    trend4.update_layout(title = 'Travel Over The Last Year',
                        xaxis_title = 'Date',
                        yaxis_title = 'Travel')

    st.plotly_chart(trend4)

def bubble_chart():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(''' SELECT username, carbon_footprint
                        FROM calculated
                        GROUP BY username
                        ORDER BY cur_date DESC
                        LIMIT 12''')
    values5 = cursor.fetchall()
    connection.close()

    val5_table = pd.DataFrame(values5, columns=['username', 'carbon_footprint'])
    val5_table_values = val5_table.groupby('username')[['carbon_footprint']].mean()

    trend5 = pe.scatter(val5_table_values, x = 'username', y = 'carbon_footprint', size = 'carbon_footprint',
                        title = 'Average Yearly Carbon Footprint of All Users',
                        size_max=60)

    st.plotly_chart(trend5)


# def drop_table(table_name):
#     connection = connection_creation()
#     cursor = connection.cursor()
#     cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
#     connection.commit()
#     connection.close()
#
# drop_table('calculated')

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

