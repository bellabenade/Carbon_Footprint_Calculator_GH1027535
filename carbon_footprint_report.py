#https://www.bing.com/videos/riverview/relatedvideo?q=how+to+create+graphs+in+streamlit&mid=30F5D319CA080E04D2E930F5D319CA080E04D2E9&FORM=VIRE

import streamlit as st
import sqlite3
import pandas as pd
import plotly.express
from database import calculate_values, herpa_derpa


def carbon_calculator():
    st.title('Carbon Footprint Report')

    cf = str(herpa_derpa())
    st.header(f'YOUR CARBON FOOTPRINT IS: {cf}')

    options = ['Dashboard', 'Recommendations', 'Energy Consumption', 'Waste Management', 'Fuel Consumption', 'How I compare to other companies?']
    selection = st.selectbox('What would you like to see?', options)

    if selection == 'Dashboard':
        pass
    elif selection == 'Recommendations':
        pass
    elif selection == 'Energy Consumption':
        pass
    elif selection == 'Waste Management':
        pass
    elif selection == 'Fuel Consumption':
        pass
    elif selection == 'How I Compare':
        pass