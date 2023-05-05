import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx

# Define the login page
def login():
    st.title('Login')

    # Get the saved username from the SessionState (if it exists)
    session_state = get_session()
    saved_username = session_state.username

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
            # Set the session state with the username
            session_state.username = username

            # Redirect the user to the app page
            st.experimental_set_query_params(logged_in=True)
        else:
            # Show an error message
            st.error('Incorrect username or password')

# Define the app page
def app():
    st.title('Welcome!')

    # Show a welcome message to the logged in user
    session_state = get_session()
    username = session_state.username
    st.write(f'Welcome, {username}!')

# Define the SessionState utility
def get_session():
    # Get the session ID hash
    ctx = get_report_ctx()
    current_code_hash = _CodeHasher.get_session_id_hash()

    # Create a session state object for the current session
    if not hasattr(ctx, 'session_state'):
        ctx.session_state = _get_state(session=current_code_hash)
    return ctx.session_state

def _get_state(**kwargs):
    return st._get_state(**kwargs)

# Check if the user is logged in
if st.experimental_get_query_params().get('logged_in'):
    app()
else:
    login()
