import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("Churn_Modelling.csv")

# Drop unused columns
data.drop(["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)

# One-hot encode categorical columns
data = pd.get_dummies(data, drop_first=True)

# Features and target
X = data.drop("Exited", axis=1)
y = data["Exited"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# Model
model = RandomForestClassifier(random_state=42)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))