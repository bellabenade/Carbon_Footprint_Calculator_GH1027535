#https://www.bing.com/videos/riverview/relatedvideo?q=how+to+create+graphs+in+streamlit&mid=30F5D319CA080E04D2E930F5D319CA080E04D2E9&FORM=VIRE

import streamlit as st
from database import herpa_derpa, pie_chart, energy_bar_chart, waste_bar_chart, travel_bar_chart, bubble_chart


def carbon_calculator():
    st.title('Carbon Footprint Report')

    cf = str(herpa_derpa())
    st.header(f'YOUR CARBON FOOTPRINT IS:')
    st.header(f'{cf}')

    st.text('\n')
    st.text('\n')

    st.subheader('MY DASHBOARD')

    pie_chart()


    options = ['Recommendations', 'Energy Consumption', 'Waste Management', 'Fuel Consumption', 'How I compare to other companies']
    selection = st.selectbox('What would you like to see?', options)

    if selection == 'Recommendations':
        pass
    elif selection == 'Energy Consumption':
        energy_bar_chart()
    elif selection == 'Waste Management':
        waste_bar_chart()
    elif selection == 'Fuel Consumption':
        travel_bar_chart()
    elif selection == 'How I Compare to other companies':
        bubble_chart()
