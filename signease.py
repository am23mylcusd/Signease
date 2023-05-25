import streamlit as st
from datetime import datetime
import os
import requests
import json

COMPLETION_KEY = "Thanks"
LOGS_FILE = "logs.txt"
WEBHOOK_URL = "https://discord.com/api/webhooks/1111120853770448896/jGdjQ5DjOsRHsS0msyrLien4LNqXpLUoC0YW2IVMKxbGrnu_4FAU48NMSOcRUyLYmm1G"

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
                with open(LOGS_FILE, 'a') as f:
                    st.session_state[COMPLETION_KEY] = True
                    date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
                    f.write(f"{date} {name} {last_name} {id} {st.session_state.choice}\n")

                # Create a payload for the Discord webhook
                payload = {
                    "content": f"{name} {last_name} {id} left to {st.session_state.choice}"
                }

                # Send a POST request to the Discord webhook URL
                response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
                if response.status_code == 204:
                    st.write("Leave information sent to Discord successfully!")
                else:
                    st.write("Failed to send leave information to Discord.")

    else:
        submit_button = st.button("Submit")
        if submit_button:
            st.session_state[COMPLETION_KEY] = True
            with open(LOGS_FILE, 'a') as f:
                date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
                f.write(f"{date} {name} {last_name} {id} returned to class\n")

            # Create a payload for the Discord webhook
            payload = {
                "content": f"{name} {last_name} {id} returned to class"
            }

            # Send a POST request to the Discord webhook URL
            response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
            if response.status_code == 204:
                st.write("Return information sent to Discord successfully!")
            else:
                st.write("Failed to send return information to Discord.")

now = datetime.now()
end_of_day = datetime(now.year, now.month, now.day, 23, 59, 0)
if now >= end_of_day:
    # Read the contents of the log file
    with open(LOGS_FILE, 'r') as f:
        logs_content = f.read()
    
    # Create a payload for the Discord webhook
    payload = {
        "content": logs_content
    }
    
    # Send a POST request to the Discord webhook URL
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    if response.status_code == 204:
        st.write("Logs uploaded to Discord successfully!")
    else:
        st.write("Failed to upload logs to Discord.")

    # Clear the log file for the next day
    with open(LOGS_FILE, 'w') as f:
        f.write("")

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
