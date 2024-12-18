from flask import Flask, render_template, request
import socket
import utils
from utils import preprocessdata

app = Flask(__name__)

@app.route('/about', endpoint='About')
def about_page():
    return render_template('About.html')

@app.route('/PredictionForm', endpoint='PredictionForm')
def prediction_form():
    return render_template('PredictionForm.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form.get('Gender')
        Married = request.form.get('Married')
        Education = request.form.get('Education')
        Self_Employed = request.form.get('Self_Employed')
        ApplicantIncome = request.form.get('ApplicantIncome')
        CoapplicantIncome = request.form.get('CoapplicantIncome')
        LoanAmount = request.form.get('LoanAmount')
        Loan_Amount_Term = request.form.get('Loan_Amount_Term')
        Credit_History = request.form.get('Credit_History')
        Property_Area = request.form.get('Property_Area')

        prediction = utils.preprocessdata(
            Gender, Married, Education, Self_Employed, ApplicantIncome,
            CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
            Property_Area
        )
        return render_template('predict.html', prediction=prediction)

def find_free_port():
    """Finds a free port on the local machine."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Bind to any available port
        return s.getsockname()[1]  # Return the port number

if __name__ == '__main__':
    port = find_free_port()
    print(f"Running on port {port}")
    app.run(port=port, debug=False, use_reloader=False)
