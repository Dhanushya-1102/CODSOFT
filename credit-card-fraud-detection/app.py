from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("fraud_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        amt = float(request.form["amt"])
        city_pop = int(request.form["city_pop"])
        gender = request.form["gender"]

        gender_value = 1 if gender == "M" else 0

        sample = pd.DataFrame([{
            "amt": amt,
            "city_pop": city_pop,
            "gender": gender_value
        }])

        result = model.predict(sample)[0]

        prediction = "🚨 Fraud Transaction" if result == 1 else "✅ Legit Transaction"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)