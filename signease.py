import streamlit as st

# Set up the cookie for storing login information
def set_user_cookie(username):
    if username:
        st.set_cookie('user', username)
    else:
        st.set_cookie('user', '', expires_at=0)

# Define the login page
def login():
    st.title('Login')

    # Get the saved username from the cookie (if it exists)
    saved_username = st.get_cookie('user')

    # Show a text input for the username
    username = st.text_input('Username', saved_username)

    # Show a password input for the password
    password = st.text_input('Password', type='password')

    # Show a "Remember Me" checkbox
    remember_me = st.checkbox('Remember Me')

    # Show a login button
    if st.button('Login'):
        # Check if the username and password are correct
        if username == 'myusername' and password == 'mypassword':
            # Set the user cookie
            set_user_cookie(username)

            # Redirect the user to the app page
            st.experimental_set_query_params(logged_in=True)
        else:
            # Show an error message
            st.error('Incorrect username or password')

# Define the app page
def app():
    st.title('Welcome!')

    # Show a welcome message to the logged in user
    username = st.get_cookie('user')
    st.write(f'Welcome, {username}!')

# Check if the user is logged in
if st.experimental_get_query_params().get('logged_in'):
    app()
else:
    login()
