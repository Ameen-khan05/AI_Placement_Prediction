import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# -----------------------------------------
# CREATE TRAINING DATA
# -----------------------------------------

np.random.seed(42)

n = 2000

cgpa = np.random.uniform(5.0, 10.0, n)
internships = np.random.randint(0, 4, n)
projects = np.random.randint(0, 5, n)
aptitude_score = np.random.uniform(30, 100, n)
skills_score = np.random.uniform(10, 100, n)


# -----------------------------------------
# PLACEMENT SCORE
# -----------------------------------------

placement_score = (
    cgpa * 10
    + internships * 8
    + projects * 6
    + aptitude_score * 0.25
    + skills_score * 0.35
)


# Students above median are considered placed
threshold = np.median(placement_score)

placed = (placement_score >= threshold).astype(int)


# -----------------------------------------
# DATAFRAME
# -----------------------------------------

df = pd.DataFrame({
    "cgpa": cgpa,
    "internships": internships,
    "projects": projects,
    "aptitude_score": aptitude_score,
    "skills_score": skills_score,
    "placed": placed
})


# -----------------------------------------
# TRAIN MODEL
# -----------------------------------------

X = df[
    [
        "cgpa",
        "internships",
        "projects",
        "aptitude_score",
        "skills_score"
    ]
]

y = df["placed"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)


# -----------------------------------------
# CHECK ACCURACY
# -----------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("--------------------------------")
print("MODEL TRAINING COMPLETE")
print("--------------------------------")
print(f"Accuracy: {accuracy * 100:.2f}%")
print("--------------------------------")


# -----------------------------------------
# SAVE MODEL
# -----------------------------------------

model_data = {
    "model": model,
    "features": [
        "cgpa",
        "internships",
        "projects",
        "aptitude_score",
        "skills_score"
    ]
}

joblib.dump(model_data, "model.pkl")

print("Model saved as model.pkl")
