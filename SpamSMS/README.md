# 📩 Spam SMS Detection Project

## 📌 Project Description
This project is a Machine Learning model that detects whether an SMS message is **Spam** or **Not Spam (Ham)**.

It uses **TF-IDF Vectorization** and **Multinomial Naive Bayes algorithm** for text classification.

---

## 📂 Dataset
File used: `spam.csv`

Columns:
- v1 → label (ham or spam)
- v2 → message text

---

## ⚙️ Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

## 🧠 Workflow
1. Load dataset
2. Clean and preprocess data
3. Convert text into numerical data using TF-IDF
4. Train model using Naive Bayes
5. Test model on new messages
6. Check accuracy

---

## 📦 Installation

## Install required libraries:
    pip install pandas scikit-learn

---

## 🚀 How to Run

Run the Python file:
python model.py
---

## 🧪 Example Prediction

Input:
Congratulations! You won free money"
Output:
Spam Message 🚨
---

## 📊 Accuracy
The model prints accuracy after training:

## Example:
Accuracy: 97.8%

---

## 🔮 Future Improvements
- Add Flask web app
- Create UI for message input
- Deploy project online
- Improve model accuracy

---

## 👨‍💻 Author
Machine Learning Project for Spam SMS Detection