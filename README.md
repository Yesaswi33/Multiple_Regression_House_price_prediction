# House Price Prediction using Flask and Machine Learning

## Overview
This project predicts house prices based on user input using a **Machine Learning (Regression) Model**. It is implemented using **Flask** for the web interface and **Scikit-Learn** for model training. The model is trained on the `Housing.csv` dataset and serves predictions via a web application.

## **Project Structure**
/regression │── app.py # Flask application to serve predictions │── train_model.py # Script to preprocess data and train the model │── Housing.csv # Dataset used for training │── preprocessed_data.pkl # Preprocessed data stored as a pickle file │── trained_model.pkl # Trained regression model │── templates/ │ ├── index.html # Frontend UI for house price prediction │── static/ │ ├── style.css # Styling for the web application │── venv/ # Virtual environment containing required libraries │── requirements.txt # List of dependencies │── README.md # Project documentation


## **Setup Instructions**
### 1️⃣ **Clone the Repository**
git clone https://github.com/Yesaswi33/Regression_House_price_prediction.git
cd Regression_House_price_prediction
### 2️⃣ Set Up Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # For MacOS/Linux
### 3️⃣ Install Dependencies
Install the required libraries using:

pip install -r requirements.txt
### 4️⃣ Run the Flask Application
python app.py
The app will be available at http://127.0.0.1:5000/.

How It Works

Train Model (train_model.py)
Loads Housing.csv
Preprocesses the data
Trains a regression model
Saves the trained model (trained_model.pkl)
Run the Flask App (app.py)
Loads the trained model
Provides a web interface (index.html)
Accepts user inputs (Square Feet, Bedrooms, Bathrooms)
Predicts the house price and displays the result
Web Interface

Users can enter property details (square feet, bedrooms, bathrooms).
Click "Predict" to get the estimated house price.
The result is displayed on the web page.
Technologies Used

Python
Flask (for Web Framework)
Pandas (for Data Handling)
Scikit-Learn (for Machine Learning)
NumPy (for Numerical Computations)
Pickle (for Model Serialization)
HTML, CSS (Frontend UI)
Future Improvements

Enhance UI with Bootstrap.
Add more features to the model (e.g., location, age of property).
Deploy the model using Heroku or AWS.
New requirements.txt File
Flask
numpy
pandas
scikit-learn
pickle-mixin
Steps to Add These Files to Git
Run the following commands in your VS Code terminal:

git add README.md requirements.txt
git commit -m "Added README and requirements.txt"
git push origin main
