import streamlit as st

# Set a key for the cookie
COOKIE_KEY = "logged_in"

# Define a function to check if the user is logged in
def is_logged_in():
    return st.session_state.get(COOKIE_KEY, False)

# Define the login form
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "Alex" and password == "M":
            st.success("Logged in!")
            # Set the cookie to True
            st.session_state[COOKIE_KEY] = True
            st.write(st.session_state.key)
            # Redirect to the homepage
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

# Define the logout function
def logout():
    # Remove the cookie
    st.session_state[COOKIE_KEY] = False
    # Redirect to the login page
    st.experimental_rerun()

# Check if the user is logged in
if is_logged_in():
    st.write("Welcome to the homepage!")
    st.button("Logout", on_click=logout)
else:
    st.write("Please login")
    login()
