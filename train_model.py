import os
import numpy as np
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Create sample placement dataset
np.random.seed(42)

n = 1000

cgpa = np.round(np.random.uniform(5.0, 10.0, n), 2)
attendance = np.round(np.random.uniform(50, 100, n), 2)
skills_score = np.round(np.random.uniform(30, 100, n), 2)
internships = np.random.randint(0, 4, n)
projects = np.random.randint(0, 5, n)
aptitude_score = np.round(np.random.uniform(30, 100, n), 2)


# Calculate a placement score
score = (
    cgpa * 10
    + attendance * 0.25
    + skills_score * 0.30
    + internships * 8
    + projects * 5
    + aptitude_score * 0.20
)

threshold = np.median(score)

placed = (score >= threshold).astype(int)


# Create DataFrame
data = pd.DataFrame({
    "cgpa": cgpa,
    "attendance": attendance,
    "skills_score": skills_score,
    "internships": internships,
    "projects": projects,
    "aptitude_score": aptitude_score,
    "placed": placed
})


# Save dataset
os.makedirs("data", exist_ok=True)

data.to_csv(
    "data/placement_data.csv",
    index=False
)


# Features and target
features = [
    "cgpa",
    "attendance",
    "skills_score",
    "internships",
    "projects",
    "aptitude_score"
]

X = data[features]
y = data["placed"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create and train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)


# Evaluate model
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)


print("--------------------------------")
print("MODEL TRAINING COMPLETE")
print("--------------------------------")
print("Accuracy:", round(accuracy * 100, 2), "%")


# Save model
model_data = {
    "model": model,
    "features": features
}

joblib.dump(
    model_data,
    "model.pkl"
)

print("Model saved as model.pkl")
print("Dataset saved as data/placement_data.csv")
