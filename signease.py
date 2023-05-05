import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

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
            url = get_server_url()
            redirect_url = url + "?page=app&logged_in=True"
            st.experimental_set_query_params(logged_in=True)
            st.experimental_rerun()

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
    # Get the session ID
    ctx = get_report_ctx()
    session_id = ctx.session_id

    # Create a session state object for the current session
    if not hasattr(ctx.session, 'my_state'):
        ctx.session.my_state = SessionState()
    return ctx.session.my_state

class SessionState:
    def __init__(self):
        self.username = None

# Get the server URL
def get_server_url():
    server = Server.get_current()
    if server is None:
        raise RuntimeError("Not running with the Streamlit server")
    return server.server_url

# Check if the user is logged in
if st.experimental_get_query_params().get('logged_in'):
    app()
else:
    login()
