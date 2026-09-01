import os
import numpy as np
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ==========================================
# CREATE TRAINING DATA
# ==========================================

np.random.seed(42)

n = 1000

cgpa = np.round(
    np.random.uniform(5.0, 10.0, n),
    2
)

internships = np.random.randint(
    0, 4, n
)

projects = np.random.randint(
    0, 5, n
)

aptitude_score = np.round(
    np.random.uniform(30, 100, n),
    2
)


# ==========================================
# SUPPORTED TECHNICAL SKILLS
# ==========================================

skills_list = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Django",
    "Flask",
    "Machine Learning",
    "Data Science",
    "Git",
    "Excel"
]


# ==========================================
# GENERATE SKILL DATA
# ==========================================

skill_data = {}

for skill in skills_list:

    skill_data[skill] = np.random.randint(
        0,
        2,
        n
    )


# ==========================================
# CALCULATE PLACEMENT SCORE
# ==========================================

skill_score = sum(
    skill_data[skill]
    for skill in skills_list
)

score = (
    cgpa * 10
    + internships * 10
    + projects * 7
    + aptitude_score * 0.25
    + skill_score * 3
)


threshold = np.median(score)

placed = (
    score >= threshold
).astype(int)


# ==========================================
# CREATE DATAFRAME
# ==========================================

data = pd.DataFrame({

    "cgpa": cgpa,

    "internships": internships,

    "projects": projects,

    "aptitude_score": aptitude_score,

    "placed": placed
})


# Add skill columns

for skill in skills_list:

    data[skill] = skill_data[skill]


# ==========================================
# SAVE DATASET
# ==========================================

os.makedirs(
    "data",
    exist_ok=True
)

data.to_csv(
    "data/placement_data.csv",
    index=False
)


# ==========================================
# FEATURES
# ==========================================

features = [
    "cgpa",
    "internships",
    "projects",
    "aptitude_score"
]

features.extend(skills_list)


X = data[features]

y = data["placed"]


# ==========================================
# SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)


# ==========================================
# TRAIN MODEL
# ==========================================

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42
)

model.fit(
    X_train,
    y_train
)


# ==========================================
# EVALUATE MODEL
# ==========================================

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)


print("--------------------------------")
print("MODEL TRAINING COMPLETE")
print("--------------------------------")

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# ==========================================
# SAVE MODEL
# ==========================================

model_data = {

    "model": model,

    "features": features,

    "skills": skills_list
}

joblib.dump(
    model_data,
    "model.pkl"
)


print("Model saved as model.pkl")

print(
    "Dataset saved as data/placement_data.csv"
)

print(
    "Available training skills:"
)

print(
    ", ".join(skills_list)
)
