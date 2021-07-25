import streamlit
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import os
import  streamlit as st

def Authenticate_user():
    filename = "wibdsoulsistersecret.json"
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, filename)
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials =  st.secrets["jsonkey"]
    #ServiceAccountCredentials.from_json_keyfile_name(filepath,
    # scopes)  # access the json key you downloaded earlier
    file = gspread.authorize(credentials)  # authenticate the JSON key with gspread
    sheet = file.open("WIBD Soul Sister Survey")  # open sheet
    sheet=sheet.sheet1
    return sheet

def Google_sheet_write(answers):
    sheet=Authenticate_user()
    max_rows = len(sheet.get_all_values()) + 1
    st.write(max_rows)
    sheet.insert_row(answers, max_rows)

def read_google_sheet():
    sheet = Authenticate_user()
    records=sheet.get_all_records()
    for record in records:
        streamlit.write(record)


