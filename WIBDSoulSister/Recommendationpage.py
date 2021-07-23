import streamlit as st
from openpyxl import load_workbook


def find_soul_sister():
    form = st.form(key='result_form')
    email = form.text_input(label='Enter WIBD email')
    ok = form.form_submit_button(label='Find your Soul sister')
    if ok :
        st.write(f'Your Soul sister is Shreya Pradhan! ')
