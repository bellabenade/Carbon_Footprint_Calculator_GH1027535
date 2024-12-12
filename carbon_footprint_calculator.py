import streamlit as st
from pages import login_page, profile

st.title('Carbon Footprint Calculator')

if st.session_state.logged_in:
    profile()
else:
    login_page()



