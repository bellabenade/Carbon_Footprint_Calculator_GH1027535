import streamlit as st


st.title('Carbon Footprint Calculator')
st.write('Gabriella Benade')
st.write('GH1027535')

st.image(".venv/Carbon_Footprint.png")
# https://si.solargaps.com/what-is-your-carbon-footprint-size/

st.header('Welcome to our Carbon Footprint Calculator!')
st.text('Thank you so much for participating in our carbon footprint survey. We hope that this analysis is just as useful to you as it is to us.')
st.write('Please click on the button to get started.')
st.write('_Please note that this information will be made public to our other existing clients. Please check the box to agree to these terms:_')
check = st.checkbox('AGREE', value = False)

if check == True:
    st.write('Agreement done!')
    start_but = st.button('__GET STARTED__')
    if start_but == True:
        st.write('_Please fill in the following information. Once completed, please click on the CALCULATE CARBON FOOTPRINT button._')

        st.subheader('Energy Usage:')
        electricity = st.text_input('What is your average monthly electricity bill in euros? ')
        nat_gas = st.text_input('What is your average monthly natural gas bill in euros? ')
        fuel = st.text_input('What is your average monthly fuel bill for transportation in euros? ')

        #energy = (electricity*12*5/10000 + nat_gas*12*53/10000 + fuel*12*232/100

        st.write(':green[___Did you know:___]')
        st.write(':green[__You can save on energy by switching off unused electrical appliances in the office!__]')
        # https://discuss.streamlit.io/t/change-font-size-and-font-color/12377

        st.subheader('Waste:')
        waste_generated = st.text_input('How much waste do you generate per month in kilograms? ')
        waste_recycled = st.text_input('How much of that waste is recycled or composted (in percentage)?')

        # waste = waste_generated*12*(0.57 - waste_recycled)

        st.write(':green[___Did you know:___]')
        st.write(':green[__You can lower your yearly waste generation by utilizing recycled materials!__]')

        st.subheader('Business Travel:')
        travel_km = st.text_input('How many kilometers do your employees travel per year for business purposes?')
        fuel_efficiency = st.text_input('What is the avergae fuel efficiency of the vehicle used for business travel in liters per 100 kilometers?')

        # travel = travel_km*(1/fuel_efficiency)*2.31

        st.write(':green[___Did you know:___]')
        st.write(':green[__You can lower your yearly waste generation by utilizing recycled materials!__]')

        st.button('CALCULATE CARBON FOOTPRINT')
else:
    st.write('Please check box to continue!')

