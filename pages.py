import streamlit as st
from User_Login import login, signup, delete

def login_page():
    st.title('Carbon Footprint Calculator')

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
        permission()
    if st.button('CALCULATE CARBON FOOTPRINT'):
        pass
    if st.button('VIEW REPORT'):
        pass
    if st.button('LOG OUT'):
        st.session_state.logged_in = False

def permission():
    st.header('Carbon Footprint Calculator')
    st.text('Thank you so much for participating in our carbon footprint survey. We hope that this analysis is just as useful to you as it is to us.')
    st.write('Click on the button to get started!')
    st.write('_Please note that this information will be made public to our other existing clients. Please check the box to agree to these terms:_')
    check = st.checkbox('AGREE', value=False)

    if check:
        if st.button('__GET STARTED__'):
            add_info()
        if st.button('BACK'):
            profile()

def add_info():
    pass
#     st.write('_Please fill in the following information. Once completed, please click on the CALCULATE CARBON FOOTPRINT button._')
#     st.subheader('Energy Usage:')
#     electricity = st.number_input('What is your average monthly electricity bill in euros?', format="%.2f")
#      nat_gas = st.number_input('What is your average monthly natural gas bill in euros?', format="%.2f")
#      fuel = st.number_input('What is your average monthly fuel bill for transportation in euros?', format="%.2f")
#
#                 # st.write(':green[___Did you know:___]')
#                 # st.write(':green[__You can save on energy by switching off unused electrical appliances in the office!__]')
#                 # https://discuss.streamlit.io/t/change-font-size-and-font-color/12377
#
#      st.subheader('Waste:')
#      waste_generated = st.number_input('How much waste do you generate per month in kilograms?', format="%.2f")
#      waste_recycled = st.number_input('How much of that waste is recycled or composted (in percentage)?', format="%.2f")
#
#                 # st.write(':green[___Did you know:___]')
#                 # st.write(':green[__You can lower your yearly waste generation by utilizing recycled materials!__]')
#
#      st.subheader('Business Travel:')
#      travel_km = st.number_input('How many kilometers do your employees travel per year for business purposes?', format="%.2f")
#      fuel_efficiency = st.number_input('What is the avergae fuel efficiency of the vehicle used for business travel in liters per 100 kilometers?', format="%.2f")
#
#                 # st.write(':green[___Did you know:___]')
#                 # st.write(':green[__You can lower your yearly waste generation by utilizing recycled materials!__]')
#
#                          # https://discuss.streamlit.io/t/take-float-input-with-number-input/14387
#      # energy = (electricity * 12 * 5 / 10000 + nat_gas * 12 * 53 / 10000 + fuel * 12 * 232 / 100)
#      # waste = waste_generated * 12 * (0.57 - waste_recycled)
#      # travel = travel_km * (1 / fuel_efficiency) * 2.31
#      #carbon_footprint = energy + waste + travel


