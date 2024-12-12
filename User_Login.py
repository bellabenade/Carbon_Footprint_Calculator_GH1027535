# gabriella_benade
# 1234
# pip freeze > requirements.txt

import streamlit as st
from database import get_user, add_user, delete_user

# validate users credentials:
def user_validation(username, password):
    user = get_user(username)
    if user and user[1] == password:
        return True
    else:
        return False

# signup function
def signup():
    st.subheader('Create a profile:')

    st.subheader('Welcome to our Carbon Footprint Calculator!')
    st.text('Thank you so much for participating in our carbon footprint survey. We hope that this analysis is just as useful to you as it is to us.')
    st.write('_Please note that this information will be made public to our other existing clients. Please check the box to agree to these terms:_')
    check = st.checkbox('AGREE', value=False)
    if check:
        new_user = st.text_input('Username:')
        new_password = st.text_input('Password:', type='password')
        if st.button('SIGNUP'):
            if get_user(new_user):
                st.error('This username already exists! Please go to login.')
            else:
                add_user(new_user, new_password)
                st.success('Signup successful! Please go to the login page and login with your new credentials.')


# login function
def login():
    st.subheader('Log into your account:')
    username = st.text_input('Username:')
    password = st.text_input('Password:', type = "password")
    if st.button('LOGIN'):
        if user_validation(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            print('You have successfully logged in!')
        else:
            st.error('Invalid username or password!')

# delete function
def delete():
    st.subheader("We're so sorry to see you go!")
    st.text('Please enter your credentials to delete your profile from our system:')
    del_user = st.text_input('Username:')
    del_password = st.text_input('Password:', type = "password")
    if st.button('DELETE'):
        if user_validation(del_user, del_password):
            delete_user(del_user)
            st.success('Your account has been deleted!')
        else:
            st.error('Username or password is invalid.')
