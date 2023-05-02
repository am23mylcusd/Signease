import streamlit as st
import json

def read_users():
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users

def write_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

def login(username, password, users):
    if username in users and users[username]['password'] == password:
        return True
    else:
        return False

def main():
    st.title("Login Page")
    st.write("Please enter your credentials to login.")
    
    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Check if username and password are correct
    if st.button("Login"):
        users = read_users()
        if login(username, password, users):
            st.success("Login successful!")
            # Create session
            session_id = username
            # Store session id in Streamlit's session state
            st.session_state['session_id'] = session_id
            # Redirect to your main application
        else:
            st.error("Invalid username or password")

if __name__ == '__main__':
    main()
