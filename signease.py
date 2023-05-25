import streamlit as st
from datetime import datetime
import requests

WEBHOOK_URL = "https://example.com/webhook"  # Replace with your webhook URL

COMPLETION_KEY = "Thanks"

if st.session_state.get(COMPLETION_KEY, False):
    st.write("Thanks")
else:
    name = st.text_input("Name")
    last_name = st.text_input("Last Name")
    student_id = st.text_input("Student ID")
    checkbox_input = st.checkbox('Signing Out?', key='my_checkbox')
    if st.session_state.my_checkbox:
        with st.form(key='my_form'):
            location_choice = st.radio("Where are you going?", ('Office', 'Bathroom', 'Other'), key='choice')
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                data = {
                    "name": name,
                    "last_name": last_name,
                    "student_id": student_id,
                    "location_choice": location_choice,
                    "timestamp": datetime.now().isoformat(),
                }
                response = requests.post(WEBHOOK_URL, json=data)
                if response.status_code == 200:
                    st.session_state[COMPLETION_KEY] = True
    else:
        submit_button = st.button("Submit")
        if submit_button:
            st.session_state[COMPLETION_KEY] = True
            data = {
                "name": name,
                "last_name": last_name,
                "student_id": student_id,
                "action": "returned to class",
                "timestamp": datetime.now().isoformat(),
            }
            response = requests.post(WEBHOOK_URL, json=data)
            if response.status_code == 200:
                st.session_state[COMPLETION_KEY] = True


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
