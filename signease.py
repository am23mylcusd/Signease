import streamlit as st

def main():
    st.title("Sign In")

    # Get the username from the user or from the cookie
    username = st.session_state.get("username")
    if not username:
        username = st.text_input("Username")
        if st.button("Sign In"):
            st.session_state["username"] = username

    # Display a welcome message to the user
    if username:
        st.write(f"Welcome back, {username}!")

if __name__ == "__main__":
    main()
