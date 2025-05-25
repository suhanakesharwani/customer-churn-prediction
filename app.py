from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        Age = int(request.form['Age'])
        Gender = 1 if request.form['Gender'] == 'Male' else 0

        Tenure = int(request.form['Tenure'])
        Usage_Frequency = int(request.form['Usage Frequency'])
        Support_Calls = int(request.form['Support Calls'])
        Payment_Delay = int(request.form['Payment Delay'])

        subscription_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
        Subscription_Type = subscription_map[request.form['Subscription Type']]

        contract_map = {'Monthly': 0, 'Quarterly': 1, 'Annual': 2}
        Contract_Length = contract_map[request.form['Contract Length']]

        Total_Spend = float(request.form['Total Spend'])
        Last_Interaction = int(request.form['Last Interaction'])

        input_data = [[
            Gender, Subscription_Type, Contract_Length,
            Age, Tenure, Usage_Frequency, Support_Calls,
            Payment_Delay, Total_Spend, Last_Interaction
        ]]

        prediction = model.predict(input_data)
        result = 'Customer Will Churn' if prediction[0] == 1 else 'Customer Will Not Churn'

        return render_template('index.html', prediction_text=result)







if __name__=="__main__":
    app.run(debug=True)