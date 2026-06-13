import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv(
    "spam.csv",
    encoding="latin-1"
)

# Select columns
data = data[["v1", "v2"]]

# Rename columns
data.columns = ["label", "message"]

# Convert labels
data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

# Features
X = data["message"]

# Target
y = data["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)

# Test sample
sample = [
    "Congratulations! You won free money"
]

result = model.predict(sample)

if result[0] == 1:
    print("Spam Message")
else:
    print("Not Spam")