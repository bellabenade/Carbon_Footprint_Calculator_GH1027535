from database import connection_creation, user_table, carbon_table, calculated, calculate_values


def insert_users(username, password):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
    connection.commit()
    connection.close()

def insert_data(username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, month, year):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO carbon (username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, month, year) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, month, year))
    connection.commit()
    connection.close()

#  # Create tables
# user_table()
# carbon_table()
# calculated()
#
#  #Insert users in table
# insert_users('Company_A', '3456')
# insert_users('Company_B', '4567')
# insert_users('Company_C', '5678')
#
# # Insert info in carbon
# insert_data('Company_A', 400, 300, 300, 600, 0, 5000, 15, 1, 2024)
# insert_data('Company_A', 300, 200, 250, 500, 0, 5000, 13, 2, 2024)
# insert_data('Company_A', 200, 100, 200, 550, 20, 4200, 10, 3, 2024)
#
# insert_data('Company_B', 250, 200, 200, 300, 30, 2000, 12, 2, 2024)
# insert_data('Company_B', 200, 100, 190, 290, 35, 1900, 11, 3, 2024)
# insert_data('Company_B', 190, 100, 170, 295, 40, 1950, 10, 4, 2024)
#
# insert_data('Company_C', 300, 200, 350, 400, 30, 3000, 11, 2, 2024)
# insert_data('Company_C', 280, 230, 320, 350, 30, 3000, 11, 3, 2024)
# insert_data('Company_C', 260, 190, 300, 380, 30, 3000, 11, 4, 2024)
#
# # Insert calculated values into table calculated
# calculate_values()

# def drop_table(table_name):
#     connection = connection_creation()
#     cursor = connection.cursor()
#     cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
#     connection.commit()
#     connection.close()
#
# drop_table('calculated')

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
print("Database Tables:")
for table in tables:
    print(table[0])

for table in tables:
    print(f"\nTable Entries:'{table[0]}':")
    entries = fetch_all_entries(table[0])
    for entry in entries:
        print(entry)