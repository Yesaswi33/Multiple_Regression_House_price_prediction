from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("models/trained_model.pkl")
scaler = joblib.load("data/preprocessed_data.pkl")[4]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(request.form['square_feet']), float(request.form['bedrooms']), float(request.form['bathrooms'])]
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)
    prediction = model.predict(data)[0]
    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
