import streamlit as st
from User_Login import login, signup, delete
from database import insert_info
from carbon_footprint_report import carbon_calculator


def login_page():
    menu = ['Please choose an action!', 'Login', 'Signup', 'Delete Profile']
    choice = st.selectbox('Please log in to continue:', menu)

    if choice == 'Signup':
        signup()
    elif choice == 'Login':
        login()
    elif choice == 'Delete Profile':
        delete()
    elif choice == 'Please choose an action!':
        st.text('Please choose an action from the dropdown list')

def profile():
    st.header(f'WELCOME, {st.session_state.username}!')
    tab1, tab2, tab3 = st.tabs(['HOME','ADD/ CHANGE INFO', 'CARBON FOOTPRINT REPORT'])

    with tab1:
        st.image('carbon_footprint.png')
        # https://si.solargaps.com/what-is-your-carbon-footprint-size/
        st.text('We are so happy to see you again!')
    with tab2:
        add_info()
    with tab3:
        carbon_calculator()
    if st.button('LOG OUT'):
        st.session_state.logged_in = False

def add_info():
    st.subheader('Please complete the following form to calculate your carbon footprint!')
    with st.form('Add_Info'):
        st.subheader('Energy Usage:')
        electricity = st.number_input('What is your average monthly electricity bill in euros?', format="%.2f")
        nat_gas = st.number_input('What is your average monthly natural gas bill in euros?', format="%.2f")
        fuel = st.number_input('What is your average monthly fuel bill for transportation in euros?', format="%.2f")

# https://discuss.streamlit.io/t/change-font-size-and-font-color/12377

        st.subheader('Waste:')
        waste_generated = st.number_input('How much waste do you generate per month in kilograms?', format="%.2f")
        waste_recycled = st.slider('How much of that waste is recycled or composted (in percentage)?', min_value= 0, max_value= 100)

        st.subheader('Business Travel:')
        travel_km = st.number_input('How many kilometers do your employees travel per year for business purposes?', format="%.2f")
        fuel_efficiency = st.number_input('What is the average fuel efficiency of the vehicle used for business travel in liters per 100 kilometers?', format="%.2f")

        cur_date = st.date_input('Select the date at which you took all these measurements:')

        submit = st.form_submit_button('SUBMIT')

    if submit:
        insert_info(st.session_state.username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, cur_date)
        st.text('Your data has been saved!')
