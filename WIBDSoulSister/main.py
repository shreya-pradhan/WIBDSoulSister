import streamlit as st
from surveypage import show_survey_questions
from Recommendationpage import find_soul_sister


menu=st.sidebar.selectbox("Menu",("Take Survey","Find your Soul Sister"))
if menu == "Take Survey" :
    show_survey_questions()
elif menu=="Find your Soul Sister" :
    find_soul_sister()