import streamlit as st
import utils
from utils import preprocessdata

# Replace Flask routes with Streamlit UI elements

def home():
    st.title("Loan Prediction")
    st.write("Welcome to the Loan Prediction App!")

def about():
    st.title("About")
    st.write("This is an app to predict loan eligibility based on various parameters.")

def prediction_form():
    st.title("Prediction Form")
    
    # Input fields
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
    ApplicantIncome = st.number_input("Applicant Income", min_value=0)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
    LoanAmount = st.number_input("Loan Amount", min_value=0)
    Loan_Amount_Term = st.selectbox("Loan Amount Term", [12, 24, 36, 48, 60])
    Credit_History = st.selectbox("Credit History", ["Yes", "No"])
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    # Prediction button
    if st.button("Predict"):
        prediction = utils.preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
                                          CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                                          Property_Area)
        st.write(f"Prediction: {prediction}")

# Mapping Streamlit pages
PAGES = {
    "Home": home,
    "About": about,
    "Prediction Form": prediction_form
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Call the selected page function
PAGES[selection]()
