import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

# This should be on top of your script
cookies = EncryptedCookieManager(
    # This prefix will get added to all your cookie names.
    # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
    prefix="localhost/",
    #prefix="",   # no prefix will show all your cookies for this domain
    # You should setup COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
    password=os.environ.get("COOKIES_PASSWORD", "Vahedidthis"),
    #password='changeme'
)

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

st.write("Current cookies:", cookies)
name = st.text_input("New name for a cookie (key)")
value = st.text_input("New value for a cookie (value)")
if st.button("Change the cookie, will save on next rerun"):
    cookies[name] = value  # This will get saved on next rerun
    if st.button("Force saving cookies now, without rerun"):
        cookies.save()  # Force saving the cookies now, without a rerun
# Set a key for the cookie
COOKIE_KEY = "logged_in"

# Define a function to check if the user is logged in
def is_logged_in():
    return st.session_state.get(COOKIE_KEY)

# Define the login form
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "Alex" and password == "M":
            st.success("Logged in!")
            # Set the cookie to True
            st.session_state[COOKIE_KEY] = True
            st.write(st.session_state[COOKIE_KEY])
            # Redirect to the homepage
            # st.experimental_rerun()
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
