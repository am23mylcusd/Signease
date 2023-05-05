import streamlit as st
import extra_streamlit_components as stx

def create_login_page():
    # Set up the login form fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check if the form has been submitted
    if st.form_submit_button("Log in"):
        if username == "myusername" and password == "mypassword":
            # Set a cookie to remember the user
            stx.set_cookies({"user": username})
            st.success("You have successfully logged in!")
            # Redirect the user to the home page
            st.experimental_set_query_params(logged_in=True)
        else:
            st.error("Invalid username or password")

def create_home_page():
    # Get the cookie for the user
    user_cookie = stx.get_cookies().get("user")

    # Check if the user is logged in
    if user_cookie is None:
        # Redirect the user to the login page
        st.experimental_set_query_params(logged_in=False)
        return

    # Display the home page
    st.write(f"Welcome back, {user_cookie}!")

def main():
    # Set up the Streamlit app
    st.set_page_config(page_title="Login Demo")
    st.title("Login Demo")

    # Determine which page to show based on the URL query parameters
    logged_in = st.experimental_get_query_params().get("logged_in")
    if logged_in == "True":
        create_home_page()
    else:
        create_login_page()

if __name__ == "__main__":
    main()
