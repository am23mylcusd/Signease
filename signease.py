import streamlit as st
from datetime import datetime
import git
import tempfile
import os

COMPLETION_KEY = "Thanks"
REPO_URL = "https://github.com/am23mylcusd/Signease.git"
TEMP_DIR = tempfile.mkdtemp()

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
                clone_repo = git.Repo.clone_from(REPO_URL, TEMP_DIR)
                with open(os.path.join(TEMP_DIR, 'logs.txt'), 'a') as f:
                    st.session_state[COMPLETION_KEY] = True
                    date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
                    f.write(f"{date} {name} {last_name} {id} {st.session_state.choice}\n")
                    clone_repo.git.add('logs.txt')
                    if clone_repo.is_dirty():
                        clone_repo.git.config('--global', 'user.email', 'amnatsakanian23@mylcusd.net')
                        clone_repo.git.config('--global', 'user.name', 'am23mylcusd')
                        clone_repo.git.commit('-m', 'Update logs.txt')
                        clone_repo.git.push()
    else:
        submit_button = st.button("Submit")
        if submit_button:
            st.session_state[COMPLETION_KEY] = True
            clone_repo = git.Repo.clone_from(REPO_URL, TEMP_DIR)
            with open(os.path.join(TEMP_DIR, 'logs.txt'), 'a') as f:
                date = datetime.now().strftime("|%m/%d/%Y - %I:%M %p|")
                f.write(f"{date} {name} {last_name} {id} returned to class\n")
                clone_repo.git.add('logs.txt')
                 if clone_repo.is_dirty():
                     clone_repo.git.config('--global', 'user.email', 'amnatsakanian23@mylcusd.net')
                     clone_repo.git.config('--global', 'user.name', 'am23mylcusd')
                     clone_repo.git.commit('-m', 'Update logs.txt')
                     clone_repo.git.push()

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
