Sure, I can help you with that. Here is an example of how to create a simple login page with cookies using "extra_streamlit_components" in Streamlit:

```python
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
```

Here's how the code works:

1. The `create_login_page` function sets up a form with two fields, one for the username and one for the password. When the form is submitted, the function checks if the username and password are correct. If they are, it sets a cookie to remember the user and redirects them to the home page. If they are not, it displays an error message.

2. The `create_home_page` function checks if there is a cookie for the user. If there is, it displays a welcome message. If there is not, it redirects the user back to the login page.

3. The `main` function sets up the Streamlit app and determines which page to show based on the URL query parameters. If the user is logged in, it shows the home page. If the user is not logged in, it shows the login page.

4. Finally, the `if __name__ == "__main__"` block ensures that the code is only executed if the file is run directly (i.e., not imported as a module).

You can run this code in your terminal with the command `streamlit run app.py` (assuming that the code is saved in a file called `app.py`).
