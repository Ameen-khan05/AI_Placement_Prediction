import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# =========================================
# AI PLACEMENT MODEL TRAINING
# =========================================

print("=" * 50)
print("       AI PLACEMENT MODEL TRAINING")
print("=" * 50)


# =========================================
# CREATE DATASET
# =========================================

np.random.seed(42)

n = 3000

cgpa = np.random.uniform(5.0, 10.0, n)

internships = np.random.randint(0, 4, n)

projects = np.random.randint(0, 5, n)

aptitude_score = np.random.uniform(30, 100, n)

skills_score = np.random.uniform(10, 100, n)


# =========================================
# CALCULATE PLACEMENT SCORE
# =========================================

placement_score = (
    cgpa * 10
    + internships * 8
    + projects * 6
    + aptitude_score * 0.25
    + skills_score * 0.35
)


# =========================================
# CREATE BALANCED TARGET
# =========================================

threshold = np.median(placement_score)

placed = (placement_score >= threshold).astype(int)


# =========================================
# CREATE DATAFRAME
# =========================================

df = pd.DataFrame({

    "cgpa": cgpa,

    "internships": internships,

    "projects": projects,

    "aptitude_score": aptitude_score,

    "skills_score": skills_score,

    "placed": placed

})


# =========================================
# FEATURES
# =========================================

features = [

    "cgpa",

    "internships",

    "projects",

    "aptitude_score",

    "skills_score"

]


X = df[features]

y = df["placed"]


# =========================================
# TRAIN / TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


# =========================================
# TRAIN RANDOM FOREST
# =========================================

model = RandomForestClassifier(

    n_estimators=300,

    max_depth=8,

    min_samples_split=5,

    min_samples_leaf=2,

    random_state=42

)


model.fit(X_train, y_train)


# =========================================
# TEST MODEL
# =========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(

    y_test,

    predictions

)


print()

print("Training records :", len(X_train))

print("Testing records  :", len(X_test))

print()

print(

    f"Model Accuracy: {accuracy * 100:.2f}%"

)

print()

print("Classification Report:")

print(

    classification_report(

        y_test,

        predictions

    )

)


# =========================================
# CHECK CLASS BALANCE
# =========================================

print()

print("Class Distribution:")

print(

    df["placed"]

    .value_counts()

    .rename({

        0: "NOT PLACED",

        1: "PLACED"

    })

)


# =========================================
# SAVE MODEL
# =========================================

model_data = {

    "model": model,

    "features": features

}


joblib.dump(

    model_data,

    "model.pkl"

)


print()

print("=" * 50)

print("Model successfully saved as:")

print("model.pkl")

print("=" * 50)