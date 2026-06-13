# 📊 Customer Churn Prediction using Machine Learning

## 🚀 Project Overview
This project predicts whether a customer will churn (leave the bank/service) or stay using a Machine Learning model (Random Forest Classifier). The model is trained on the Churn Modelling dataset and uses preprocessing, encoding, training, and evaluation steps.

---

## 📁 Dataset
File: `Churn_Modelling.csv`

### Important Columns:
- RowNumber ❌ (removed)
- CustomerId ❌ (removed)
- Surname ❌ (removed)
- CreditScore
- Geography 🌍
- Gender 👤
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary
- Exited 🎯 (Target)

---

## ⚙️ Technologies Used
- Python 🐍
- Pandas 📊
- Scikit-learn 🤖
- RandomForestClassifier 🌳

---

## 🧠 Machine Learning Model
We used:
- RandomForestClassifier from sklearn

---

## 🔄 Workflow
1. Load dataset
2. Drop unnecessary columns
3. Encode categorical features
4. Split dataset into training and testing sets
5. Train Random Forest model
6. Make predictions
7. Calculate accuracy

---

## 📦 Installation

Install required libraries:

```bash
pip install pandas scikit-learn
```

---

## ▶️ How to Run

Run the script:

```bash
python churn_model.py
```

---

## 📊 Output Example

```
Accuracy: 0.85 (approx)
```

---

## ⚠️ Common Issues

### ❌ Error: could not convert string to float ('France')
✔ Fix: Use `pd.get_dummies()` or proper encoding

### ❌ Error: 'Exited' column not found
✔ Fix:
```python
print(data.columns)
```

---

## 📈 Future Improvements
- Hyperparameter tuning
- Confusion matrix
- ROC-AUC score
- Flask / FastAPI deployment
- Frontend UI for predictions

---

## 👨‍💻 Author
Machine Learning Mini Project