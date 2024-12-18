#https://www.bing.com/videos/riverview/relatedvideo?q=how+to+create+graphs+in+streamlit&mid=30F5D319CA080E04D2E930F5D319CA080E04D2E9&FORM=VIRE

import streamlit as st
from database import pie_chart, energy_bar_chart, \
    connection_creation, waste_bar_chart, \
    travel_bar_chart, bubble_chart, cf_calculation
from pdf_generator import create_pdf
from recommendations import recommendations


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

    displayed_year = st.selectbox('Enter the year of which you want to see results: ', options=list(range(2020, 2050)))

    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT *
                            FROM carbon
                            WHERE year = {displayed_year}''')
    exist = cursor.fetchall()
    connection.close()

    if exist:
        selection = st.selectbox('What would you like to see?', options = ['Recommendations', 'Energy Consumption', 'Waste Management', 'Fuel Consumption', 'How I compare to other companies', 'Download Report for This Year'])

        if selection == 'Recommendations':
            monthly_df, diff_html, total_change = recommendations(displayed_year)
            st.subheader('Your data for the past 12 months:')
            st.table(monthly_df)
            st.subheader('Change in monthly consumption:')
            st.markdown(diff_html, unsafe_allow_html = True)
            st.subheader('Your total change in consumption over the last year:')
            st.markdown(total_change, unsafe_allow_html = True)
            st.subheader('You can consider the following recommendations:')


        elif selection == 'Energy Consumption':
            energy_bar = energy_bar_chart(displayed_year)
            st.plotly_chart(energy_bar)
        elif selection == 'Waste Management':
            waste_bar = waste_bar_chart(displayed_year)
            st.plotly_chart(waste_bar)
        elif selection == 'Fuel Consumption':
            travel_bar = travel_bar_chart(displayed_year)
            st.plotly_chart(travel_bar)
        elif selection == 'How I compare to other companies':
            cf_bubble = bubble_chart(displayed_year)
            st.plotly_chart(cf_bubble)
        elif selection == 'Download Report for This Year':
            pass
            # print('1')
            # pdf_data = create_pdf()
            # print(pdf_data)
            # st.download_button('DOWNLOAD CARBON FOOTPRINT REPORT',
            #                       data = pdf_data,
            #                       file_name = 'carbon_footprint_report.pdf',
            #                       mime = 'application/pdf')
    else:
        st.text('You do not have any data for the specified year!')
