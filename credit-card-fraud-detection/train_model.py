import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("Loading dataset...")

df = pd.read_csv("fraudTest.csv")

# Keep only important columns
df = df[["amt", "city_pop", "gender", "is_fraud"]]

# Encode gender
df["gender"] = df["gender"].map({"M": 1, "F": 0})

df = df.dropna()

print("Class distribution:")
print(df["is_fraud"].value_counts())

# BALANCE DATASET (IMPORTANT FIX)
fraud = df[df["is_fraud"] == 1]
legit = df[df["is_fraud"] == 0].sample(len(fraud))

df = pd.concat([fraud, legit])

X = df[["amt", "city_pop", "gender"]]
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "fraud_model.pkl")

print("Model saved successfully!")