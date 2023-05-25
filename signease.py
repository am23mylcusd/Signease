import streamlit as st
import smtplib
from email.message import EmailMessage
from datetime import datetime

COMPLETION_KEY = "Thanks"

def send_email(message):
    sender_email = "keithleyclassbot@gmail.com"  # Replace with your email address
    sender_password = "Keithleyrocks123%%"  # Replace with your email password
    receiver_email = "amnatsakanian23@mylcusd.net"  # Replace with your teacher's email address

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "Student Activity"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        st.write("Email sent successfully!")
    except Exception as e:
        st.write(f"Error sending email: {e}")

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
