import streamlit as st
from User_Login import login, signup, delete
from database import insert_info, calculate_values
from carbon_footprint_report import carbon_calculator


def initialize():
    st.title('Carbon Footprint Calculator')

    if 'initialize' not in st.session_state:
        st.session_state.initialize = True
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ''


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
        st.session_state.initialize = True
        st.session_state.username = ''

def add_info():
    submit = False
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

        month = st.selectbox('Month', options= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
        year = st.selectbox('Year', options= list(range(2020, 2050)))

        if st.form_submit_button('SUBMIT'):
            submit = True

    if submit:
        insert_info(st.session_state.username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency, month, year)
        calculate_values()
        st.text('Your data has been saved!')
        submit = False
