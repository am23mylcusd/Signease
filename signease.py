import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

# This should be on top of your script
cookies = EncryptedCookieManager(
    # This prefix will get added to all your cookie names.
    # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
    prefix="localhost/",
    #prefix="",   # no prefix will show all your cookies for this domain
    # You should setup COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
    #password=os.environ.get("COOKIES_PASSWORD", "Vahedidthis"),
    password='changeme'
)

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

# Set a key for the cookie
COOKIE_KEY = "logged_in"

def signup():
    name = st.text_input("Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("School Email")
    if st.button("Sign Up!"):
        st.session_state[COOKIE_KEY] = True
        cookies[name] = {last_name,email,st.session_state[COOKIE_KEY]}
        cookies.save()


# Define a function to check if the user is logged in
def is_logged_in():
    return cookies["alex"][2]

# Define the login form
def login():
    name = st.text_input("Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("School Email")
    if st.button("Login"):
        if name in cookies and last_name == cookies[username][0] and email == cookies[username][1]:
            # Set the cookie to True
            st.session_state[COOKIE_KEY] = True
            cookies[name][2] = st.session_state[COOKIE_KEY]
            # Redirect to the homepage
            # st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

# Define the logout function
def logout():
    # Remove the cookie
    st.session_state[COOKIE_KEY] = False
    cookies["alex"][2] = st.session_state[COOKIE_KEY]
    # Redirect to the login page
    st.experimental_rerun()       
        
        
st.write("Current cookies:", cookies, cookies.keys())
st.button("Sign up", on_click=signup)

# st.write("Current cookies:", cookies)
# name = st.text_input("New name for a cookie (key)")
# value = st.text_input("New value for a cookie (value)")
# if st.button("Change the cookie, will save on next rerun"):
#     cookies[name] = value  # This will get saved on next rerun
#     if st.button("Force saving cookies now, without rerun"):
#         cookies.save()  # Force saving the cookies now, without a rerun


# Check if the user is logged in

if is_logged_in():
    st.write("Welcome to the homepage!")
    st.button("Logout", on_click=logout)
else:
    st.write("Please login")
    login()
