import streamlit as st
import os

def home():
    # Load the 'index.html' from the 'templates' folder
    with open(os.path.join("templates", "index.html"), "r") as file:
        home_html = file.read()
    st.markdown(home_html, unsafe_allow_html=True)

def about():
    # Load the 'About.html' from the 'templates' folder
    with open(os.path.join("templates", "About.html"), "r") as file:
        about_html = file.read()
    st.markdown(about_html, unsafe_allow_html=True)

def prediction_form():
    # Load the 'PredictionForm.html' from the 'templates' folder
    with open(os.path.join("templates", "PredictionForm.html"), "r") as file:
        prediction_form_html = file.read()
    st.markdown(prediction_form_html, unsafe_allow_html=True)

# Directly call the home function to display the home page
home()
