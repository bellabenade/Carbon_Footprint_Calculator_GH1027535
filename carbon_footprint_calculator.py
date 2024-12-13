import streamlit as st
from pages import login_page, profile

st.title('Carbon Footprint Calculator')

login_page()
if st.session_state.logged_in:
    profile()






