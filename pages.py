import streamlit as st
from streamlit import session_state
from User_Login import login, signup, delete
from database import insert_info


def login_page():
    st.title('Carbon Footprint Calculator')

    st.image('carbon_footprint.png')
    # https://si.solargaps.com/what-is-your-carbon-footprint-size/

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
    st.title('Carbon Footprint Calculator')
    st.text('What would you like to do?')
    if st.button('ADD/ CHANGE INFO'):
        add_info()
    if st.button('CARBON FOOTPRINT REPORT'):
        pass
    if st.button('LOG OUT'):
        st.session_state.logged_in = False

def add_info():
    with st.form('Please complete the following form then click on the SUBMIT button:'):
        st.subheader('Energy Usage:')
        electricity = st.number_input('What is your average monthly electricity bill in euros?', format="%.2f")
        nat_gas = st.number_input('What is your average monthly natural gas bill in euros?', format="%.2f")
        fuel = st.number_input('What is your average monthly fuel bill for transportation in euros?', format="%.2f")

# https://discuss.streamlit.io/t/change-font-size-and-font-color/12377

        st.subheader('Waste:')
        waste_generated = st.number_input('How much waste do you generate per month in kilograms?', format="%.2f")
        waste_recycled = st.number_input('How much of that waste is recycled or composted (in percentage)?', format="%.2f")

        st.subheader('Business Travel:')
        travel_km = st.number_input('How many kilometers do your employees travel per year for business purposes?', format="%.2f")
        fuel_efficiency = st.number_input('What is the average fuel efficiency of the vehicle used for business travel in liters per 100 kilometers?', format="%.2f")

# https://discuss.streamlit.io/t/take-float-input-with-number-input/14387

        submit = st.form_submit_button('SUBMIT')

    if submit:
        if not electricity:
            st.text('Please complete the ENERGY section! There seems to be information missing...')
        elif not nat_gas:
            st.text('Please complete the ENERGY section! There seems to be information missing...')
        elif not fuel:
            st.text('Please complete the ENERGY section! There seems to be information missing...')
        elif not waste_generated:
            st.text('Please complete the WASTE section! There seems to be information missing...')
        elif not waste_recycled:
            st.text('Please complete the WASTE section! There seems to be information missing...')
        elif not travel_km:
            st.text('Please complete the TRAVEL section! There seems to be information missing...')
        elif not fuel_efficiency:
            st.text('Please complete the TRAVEL section! There seems to be information missing...')
        elif st.session_state.username:
            insert_info(st.session_state.logged_in.username, electricity, nat_gas, fuel, waste_generated, waste_recycled, travel_km, fuel_efficiency)
        else:
            print('Not logged in!')
        # try:
        #     energy = (electricity * 12 * 5 / 10000 + nat_gas * 12 * 53 / 10000 + fuel * 12 * 232 / 100)
        #     waste = waste_generated * 12 * (0.57 - waste_recycled)
        #     travel = travel_km * (1 / fuel_efficiency) * 2.31
        # except ZeroDivisionError:
        #     print('Please fill in all required values!')
        # except ValueError:
        #     print('Please enter valid number with a comma (,) to show decimal numbers')

# def carbon_footprint():
#     st.title('YOUR CARBON FOOTPRINT IS: ', carbon_footprint)





