import streamlit as st
import smtplib, ssl
from datetime import datetime

COMPLETION_KEY = "Thanks"

def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "keithleyclassbot@gmail.com"  # Replace with your email address
    password = "Keithleyrocks123%%"  # Replace with your email password
    receiver_email = "amnatsakanian23@mylcusd.net"  # Replace with your teacher's email address

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if st.session_state.get(COMPLETION_KEY, False):
    st.write("Thanks")
else:
    name = st.text_input("Name")
    last_name = st.text_input("Last Name")
    id = st.text_input("Student ID")
    checkbox_input = st.checkbox('Signing Out?', key='my_checkbox')
    if st.session_state.my_checkbox:
        with st.form(key='my_form'):
            st.radio("Where are you going?", ('Office', 'Bathroom', 'other'), key='choice')
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                st.session_state[COMPLETION_KEY] = True
                date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
                message = f"{date} {name} {last_name} {id} {st.session_state.choice}"
                send_email(message)
    else:
        submit_button = st.button("Submit")
        if submit_button:
            st.session_state[COMPLETION_KEY] = True
            date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
            message = f"{date} {name} {last_name} {id} returned to class"
            send_email(message)

# import streamlit as st
# from datetime import datetime


# COMPLETION_KEY = "Thanks"

# if st.session_state.get(COMPLETION_KEY, False):
#     st.write("Thanks")
# else:
#     name = st.text_input("Name")
#     last_name = st.text_input("Last Name")
#     id = st.text_input("Student ID")
#     checkbox_input = st.checkbox('Signing Out?', key='my_checkbox')
#     if st.session_state.my_checkbox == True:
#         with st.form(key='my_form'):
#             st.radio("Where are you going?", ('Office', 'Bathroom', 'other'), key='choice')
#             submit_button = st.form_submit_button(label='Submit')
#             if submit_button:
#                 with open('logs.txt', 'a') as f:
#                     st.session_state[COMPLETION_KEY] = True
#                     date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
#                     f.write(f"{date} {name} {last_name} {id} {st.session_state.choice}\n")
#     else:
#         submit_button = st.button("Submit")
#         if submit_button:
#             st.session_state[COMPLETION_KEY] = True
#             with open('logs.txt', 'a') as f:
#                 date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
#                 f.write(f"{date} {name} {last_name} {id} returned to class\n")
