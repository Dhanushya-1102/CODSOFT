# Credit Card Fraud Detection Using Machine Learning

This is a Machine Learning + Flask web application that predicts whether a transaction is **Fraud** or **Legit** based on user input.

---

## Features
- Fraud vs Legit transaction prediction
- Machine Learning model (Random Forest)
- Web interface using Flask
- Real-time predictions
- Balanced dataset handling

---

## Tech Stack
- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML

---

## Project Structure
fraud-detection/
│
├── app.py
├── train_model.py
├── fraud_model.pkl
├── fraudTest.csv
├── templates/
│     └── index.html
└── README.md

---

## Installation

pip install flask pandas scikit-learn joblib

---

## Train Model

python train_model.py

This will:
- Load dataset
- Balance data
- Train Random Forest model
- Save model as fraud_model.pkl

---

## Run Application

python app.py

Open browser:
http://127.0.0.1:5000/

---

## Input Fields
- Amount
- City Population
- Gender

---

## Output
- Fraud Transaction 🚨
- Legit Transaction ✅

---

## Example Inputs

### Legit Transaction
Amount: 200  
City Population: 50000  
Gender: Female  

### Fraud Transaction
Amount: 9000  
City Population: 100  
Gender: Male  

---

## Note
This project is for learning purposes. Model accuracy depends on dataset quality and feature selection.

---

## Author
Student Project - Machine Learning + Flask