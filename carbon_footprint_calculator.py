import streamlit as st
from pages import initialize, login_page, profile


initialize()

if st.session_state.initialize:
    login_page()
elif st.session_state.logged_in:
    profile()

