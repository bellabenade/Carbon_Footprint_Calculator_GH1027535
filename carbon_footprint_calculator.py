import streamlit as st
from streamlit import session_state

from User_Login import login, signup, delete
from pages import login_page, profile

login_page()

if st.session_state.logged_in:
    profile()
else:
    login_page()

if st.session_state.add_ifo:




# Login page
# menu = ['Login', 'Signup', 'Delete Profile']
# choice = st.selectbox('Please log in to continue:', menu)
#
# if choice == 'Signup':
#     signup()
# elif choice == 'Login':
#     login()
# elif choice == 'Delete Profile':
#     delete()

    # st.image(".venv/Carbon_Footprint.png")
    # https://si.solargaps.com/what-is-your-carbon-footprint-size/

# if signing up: take user to page where info is collected.
# 1. go to log in
# 2. ask for company information
# 3. calculate carbon footprint
# 4. show page with different elements calculated with recommendations to reduce carbon footprint
# 5. show comparison to other companies
# 6. download report in pdf format

# if logging in: show already existing information with an option to change the information
# 1. Take directly to page with elements and recommendations
# 2. Compare to other companies
# 3. Button to change information
# 4. download report in pdf format

# if deleting: remove all information regarding the user as well as access to info regarding other users

# st.header('Welcome to our Carbon Footprint Calculator!')
# st.text('Thank you so much for participating in our carbon footprint survey. We hope that this analysis is just as useful to you as it is to us.')
# st.write('Please click on the button to get started.')
# st.write('_Please note that this information will be made public to our other existing clients. Please check the box to agree to these terms:_')
# check = st.checkbox('AGREE', value = False)
# if check:
#     st.write('Agreement done!')
#     start_but = st.button('__GET STARTED__')
#     if start_but:
#         with st.form('Carbon Footprint'):
#             st.write('_Please fill in the following information. Once completed, please click on the CALCULATE CARBON FOOTPRINT button._')
#
#             st.subheader('Energy Usage:')
#             electricity = st.number_input('What is your average monthly electricity bill in euros?', format = "%.2f")
#             nat_gas = st.number_input('What is your average monthly natural gas bill in euros?', format = "%.2f")
#             fuel = st.number_input('What is your average monthly fuel bill for transportation in euros?', format = "%.2f")
#
#             # st.write(':green[___Did you know:___]')
#             # st.write(':green[__You can save on energy by switching off unused electrical appliances in the office!__]')
#             # https://discuss.streamlit.io/t/change-font-size-and-font-color/12377
#
#             st.subheader('Waste:')
#             waste_generated = st.number_input('How much waste do you generate per month in kilograms?', format = "%.2f")
#             waste_recycled = st.number_input('How much of that waste is recycled or composted (in percentage)?', format = "%.2f")
#
#             # st.write(':green[___Did you know:___]')
#             # st.write(':green[__You can lower your yearly waste generation by utilizing recycled materials!__]')
#
#             st.subheader('Business Travel:')
#             travel_km = st.number_input('How many kilometers do your employees travel per year for business purposes?', format = "%.2f")
#             fuel_efficiency = st.number_input('What is the avergae fuel efficiency of the vehicle used for business travel in liters per 100 kilometers?', format = "%.2f")
#
#             # st.write(':green[___Did you know:___]')
#             # st.write(':green[__You can lower your yearly waste generation by utilizing recycled materials!__]')
#
#             submitted = st.form_submit_button('CALCULATE CARBON FOOTPRINT')
#             if submitted:
#                 #https://discuss.streamlit.io/t/take-float-input-with-number-input/14387
#                 energy = (electricity*12*5/10000 + nat_gas*12*53/10000 + fuel*12*232/100)
#                 waste = waste_generated*12*(0.57 - waste_recycled)
#                 travel = travel_km*(1/fuel_efficiency)*2.31
#                 carbon_footprint = energy+waste+travel
#                 st.text(carbon_footprint)
#     else:
#         st.write('Please check box to continue!')
#
# else:
#     st.text('Please login to continue')


