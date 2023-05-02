import streamlit as st

def main():
    st.title("Sign In")

    # Get the username from the user
    username = st.text_input("Username")

    # Check if the user has signed in before
    if st.session_state.get("signed_in"):
        st.write(f"Welcome back, {username}!")
    else:
        # If the user has not signed in before, display a sign-in button
        if st.button("Sign In"):
            st.session_state["signed_in"] = True
            st.write(f"Welcome, {username}!")

if __name__ == "__main__":
    main()
