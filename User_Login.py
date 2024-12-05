import streamlit as st

# Initialize user data storage
if "users" not in st.session_state:
    st.session_state.users = {}

# Signup function
def signup(username, password):
    if username in st.session_state.users:
        return False, "Username already exists!"
    else:
        st.session_state.users[username] = password
        return True, "Signup successful!"

# Login function
def login(username, password):
    if username in st.session_state.users:
        if st.session_state.users[username] == password:
            return True, "Login successful!"
        else:
            return False, "Incorrect password!"
    else:
        return False, "Username does not exist!"

# User Interface
st.title("Carbon Footprint Calculator")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("What are you doing?", menu)

if choice == "Signup":
    st.subheader("Are you a new member?")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    if st.button("Signup"):
        success, message = signup(new_user, new_password)
        st.success(message) if success else st.error(message)

elif choice == "Login":
    st.subheader("Login to your account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        success, message = login(username, password)
        st.success(message) if success else st.error(message)

    if success:
        st.write(f"Welcome, {username}!")

st.write("Registered Users:")
st.write(st.session_state.users)
