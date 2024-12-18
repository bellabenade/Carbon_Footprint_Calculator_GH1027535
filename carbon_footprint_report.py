#https://www.bing.com/videos/riverview/relatedvideo?q=how+to+create+graphs+in+streamlit&mid=30F5D319CA080E04D2E930F5D319CA080E04D2E9&FORM=VIRE

import streamlit as st
from database import pie_chart, energy_bar_chart, \
    connection_creation, waste_bar_chart, \
    travel_bar_chart, bubble_chart, cf_calculation
from pdf_generator import create_pdf
from recommendations import data_tables


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
        selection = st.selectbox('What would you like to see?', options = ['Data and Recommendations', 'Energy Consumption', 'Waste Management', 'Fuel Consumption', 'How I compare to other companies', 'Download Report for This Year'])

        if selection == 'Data and Recommendations':
            monthly_df, diff_html, total_change, energy_con, waste_gen, travel_con, carbon_ft = data_tables(displayed_year)
            st.subheader('Your data for the past 12 months:')
            st.text('This is the data that you provided us for the past 12 months.')
            st.table(monthly_df)
            st.subheader('Change in monthly consumption:')
            st.text('This table shows how your consumption has changed from the previous month.')
            st.markdown(diff_html, unsafe_allow_html = True)
            st.subheader('Your total change in consumption over the last year:')
            st.text("Here you can see your total change from the beginning until the end of the year. Let's see how you did!")
            st.markdown(total_change, unsafe_allow_html = True)
            st.subheader('You can consider the following recommendations:')
            st.subheader('Recommendations:')
            if energy_con > 0:
                st.text('We see there has been an increase in your energy consumption. Maybe keep the following recommendations in mind:')
                st.text('* Switch off all unnecessary appliances (in the office AND the lab) if it is not being used.')
                st.text('* Consider utilizing environmentally friendly energy sources, such as solar power, if possible.')
                st.text("* Don't let privileges , such as air-conditioning be abused by employees. Maybe crack a window in the summer time, in stead of constantly utilizing air-conditioning.")
                st.text("* If it is possible, consider allowing employees to work from home occasionally to save on fuel costs and office space")
            if waste_gen > 0:
                st.text('We see there has been an increase in your waste generation. Maybe keep the following recommendations in mind:')
                st.text('* Assess if there is more waste that could be recycled at your company. If you have chemical waste, you are welcome to contact us to dispose of your waste safely and economically!')
                st.text('* Is it possible that some of your waste materials can be reused? It would not only be better for the environment, but can save you some industrial costs...')
                st.text('* Identify what could have been a possible cause for the increase in waste generation. Was this only a once-off situation? If there is an increase every month, maybe investigate internally to identify what lead to this.')
            if travel_con > 0:
                st.text('We see there has been an increase in your energy consumption. Maybe keep the following recommendations in mind:')
                st.text('*How efficient are your vehicles? It is always important to do regular maintenance on it and make sure that it is in optimal condition.')
                st.text('*How fuel-efficient are your vehicles? Have you considered getting rid of vehicles with poor fuel efficiency and finding something that is more environmentally friendly?')
                st.text('*Is there sufficient control over the use of company vehicles? Can your employees use the vehicles at their own discretion, or is there a process to approve the use thereof? If not, consider creating or updating your process.')
                st.text('*If employees utilize their own vehicles, is there an approval process to manage vehicle usage for business purposes? If not, consider creating or updating your process.')
                st.text('* If vehicles are rented, is the efficiency of the vehicle taken into account when selecting an option? Consider making this a part of the process.')

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
