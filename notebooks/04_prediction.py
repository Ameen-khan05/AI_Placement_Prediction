import pandas as pd
import joblib

# ==============================
# LOAD TRAINED MODEL
# ==============================

model = joblib.load("model.pkl")

print("===== MODEL LOADED =====")
print("Trained model loaded successfully!")


# ==============================
# LOAD CLEANED DATASET
# ==============================

df = pd.read_csv("data/placement_data_cleaned.csv")

# Get all input columns
feature_columns = df.drop("Placement", axis=1).columns

print("\n===== INPUT FEATURES =====")
print(feature_columns.tolist())


# ==============================
# CREATE NEW STUDENT DATA
# ==============================

# Use the first student's values as an example
student = df.drop("Placement", axis=1).iloc[[0]]


print("\n===== STUDENT DATA =====")
print(student)


# ==============================
# MAKE PREDICTION
# ==============================

prediction = model.predict(student)
probability = model.predict_proba(student)

print("\n===== PREDICTION PROBABILITY =====")
print(f"Not Placed: {probability[0][0] * 100:.2f}%")
print(f"Placed: {probability[0][1] * 100:.2f}%")


# ==============================
# DISPLAY RESULT
# ==============================

print("\n===== PREDICTION RESULT =====")

if prediction[0] == 1:
    print("Student is likely to be PLACED")
else:
    print("Student is likely NOT TO BE PLACED")