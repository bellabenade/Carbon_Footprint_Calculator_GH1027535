from database import connection_creation
import streamlit as st
import pandas as pd


def data_tables(year):
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT year, month, energy, waste, travel, carbon_footprint
                        FROM calculated
                        WHERE username = '{st.session_state.username}' AND (year = {year} OR year = {year-1})
                        ORDER BY year ASC, month ASC
                        LIMIT 12''')
    monthly_data = cursor.fetchall()
    connection.close()

    monthly_data_df1 = pd.DataFrame(monthly_data, columns= ['Year', 'Month', 'Energy Consumption', 'Waste Generation', 'Travel Consumption', 'Carbon Footprint']).astype(int)

    monthly_data_df2 = monthly_data_df1.copy()
    monthly_data_df2['Monthly Change in Energy Consumption (%)'] = monthly_data_df2['Energy Consumption'].pct_change().fillna(0)*100
    monthly_data_df2['Monthly Change in Waste Generation (%)'] = monthly_data_df2['Waste Generation'].pct_change().fillna(0)*100
    monthly_data_df2['Monthly Change in Travel Consumption (%)'] = monthly_data_df2['Travel Consumption'].pct_change().fillna(0)*100
    monthly_data_df2['Monthly Change in Carbon Footprint (%)'] = monthly_data_df2['Carbon Footprint'].pct_change().fillna(0)*100

    def fill_colour(table_value):
        if table_value > 0:
            return 'background-color: red'
        elif table_value < 0:
            return 'background-color: green'
        else:
            return 'background-color: blue'

    monthly_difference_df = monthly_data_df2[
        ['Year', 'Month', 'Monthly Change in Energy Consumption (%)', 'Monthly Change in Waste Generation (%)', 'Monthly Change in Travel Consumption (%)', 'Monthly Change in Carbon Footprint (%)']].drop(index = 0).astype(int)
    monthly_difference_df = monthly_difference_df.style.applymap(fill_colour, subset = ['Monthly Change in Energy Consumption (%)', 'Monthly Change in Waste Generation (%)', 'Monthly Change in Travel Consumption (%)', 'Monthly Change in Carbon Footprint (%)'])
    monthly_difference_df = monthly_difference_df.set_properties(**{'text-align': 'right'})

    total_change = {'Monthly Change in Energy Consumption (%)': monthly_data_df2['Monthly Change in Energy Consumption (%)'].sum(),
                    'Monthly Change in Waste Generation (%)': monthly_data_df2['Monthly Change in Waste Generation (%)'].sum(),
                    'Monthly Change in Travel Consumption (%)': monthly_data_df2['Monthly Change in Travel Consumption (%)'].sum(),
                    'Monthly Change in Carbon Footprint (%)': monthly_data_df2['Monthly Change in Carbon Footprint (%)'].sum()}

    total_change_df = pd.DataFrame(total_change, columns= ['Monthly Change in Energy Consumption (%)', 'Monthly Change in Waste Generation (%)', 'Monthly Change in Travel Consumption (%)', 'Monthly Change in Carbon Footprint (%)'],index = [0])
    total_change_df = total_change_df.style.applymap(fill_colour).set_properties(**{'text-align': 'right'})

    monthly_diff = monthly_difference_df.to_html()
    total_change_html = total_change_df.to_html()

    energy_consumption = total_change['Monthly Change in Energy Consumption (%)']
    waste_generation = total_change['Monthly Change in Waste Generation (%)']
    travel_consumption = total_change['Monthly Change in Travel Consumption (%)']
    carbon_footprint = total_change['Monthly Change in Carbon Footprint (%)']

    return monthly_data_df1, monthly_diff, total_change_html, energy_consumption, waste_generation, travel_consumption, carbon_footprint

