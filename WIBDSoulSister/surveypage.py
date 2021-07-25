import streamlit as st
from Excelreader import write_local_file,read_local_files
from GoogleSheetReader import read_google_sheet,Google_sheet_write

def show_survey_questions() :

    userform = st.form(key='user-form')
    email=userform.text_input(label='Enter WIBD email')
    kryptonite = userform.selectbox('What is your kryptonite?',('Procrastination', 'Perfectionism', 'Self-doubt','Lack of focus','Lack of follow-through'))
    success = userform.selectbox('How do you define success?',('Flying first class', 'Finding my purpose in life', 'Having a family that loves me'))
    energy = userform.selectbox('When do you have the best energy?',('6am-12pm', '12pm-6pm', '6pm-Midnight','Midnight-6am'))
    socialmedia = userform.selectbox('What is your favorite social media network?',('Twitter','Facebook','Instagram','Snapchat','LinkedIn'))
    submit_button = userform.form_submit_button(label='Submit')

    if(submit_button) :
        answers = [email, kryptonite, success, energy, socialmedia]
        Google_sheet_write(answers)
        read_google_sheet()




