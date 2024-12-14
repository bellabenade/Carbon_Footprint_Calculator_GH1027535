#https://www.bing.com/videos/riverview/relatedvideo?q=how+to+create+graphs+in+streamlit&mid=30F5D319CA080E04D2E930F5D319CA080E04D2E9&FORM=VIRE

import streamlit as st
from database import pie_chart, energy_bar_chart, \
    connection_creation, waste_bar_chart, \
    travel_bar_chart, carbon_footprint_bar_chart, cf_calculation
from pdf_generator import create_pdf


def carbon_calculator():
    st.title('Carbon Footprint Report')

    cf = str(cf_calculation())
    st.header(f'YOUR CARBON FOOTPRINT IS:')
    st.header(f'{cf}')

    st.text('\n')
    st.text('\n')

    st.subheader('MY DASHBOARD')


    pie_ch = pie_chart()
    st.plotly_chart(pie_ch)

    year = st.selectbox('Enter the year of which you want to see results: ', options=list(range(2020, 2050)))

    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT *
                            FROM carbon
                            WHERE year = {year}''')
    exist = cursor.fetchall()
    connection.close()

    if exist:
        selection = st.selectbox('What would you like to see?', options = ['Recommendations', 'Energy Consumption', 'Waste Management', 'Fuel Consumption', 'How I compare to other companies', 'Download Report for This Year'])

        if selection == 'Recommendations':
            pass
        elif selection == 'Energy Consumption':
            energy_bar = energy_bar_chart(year)
            st.plotly_chart(energy_bar)
        elif selection == 'Waste Management':
            waste_bar = waste_bar_chart(year)
            st.plotly_chart(waste_bar)
        elif selection == 'Fuel Consumption':
            travel_bar = travel_bar_chart(year)
            st.plotly_chart(travel_bar)
        elif selection == 'How I Compare to other companies':
            cf_bar = carbon_footprint_bar_chart(year)
            st.plotly_chart(cf_bar)
        elif selection == 'Download Report for This Year':
            pdf_data = create_pdf()
            if st.download_button('DOWNLOAD CARBON FOOTPRINT REPORT'):
                st.text('well done!')
    else:
        st.text('You do not have any data for the specified year!')


