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


# =================================
# CREATE NEW STUDENT DATA
# =================================

print("\n===== ENTER STUDENT DETAILS =====")

student_id = int(input("Student ID: "))
cgpa = float(input("CGPA: "))
tenth_percentage = float(input("10th Percentage: "))
twelfth_percentage = float(input("12th Percentage: "))
backlogs = int(input("Backlogs: "))
internship = int(input("Internship (0 = No, 1 = Yes): "))
projects = int(input("Projects: "))
technical_skills = int(input("Technical Skills: "))
communication_skills = int(input("Communication Skills: "))
aptitude_score = float(input("Aptitude Score: "))
attendance = float(input("Attendance: "))

student = pd.DataFrame([[
    student_id,
    cgpa,
    tenth_percentage,
    twelfth_percentage,
    backlogs,
    internship,
    projects,
    technical_skills,
    communication_skills,
    aptitude_score,
    attendance
]], columns=feature_columns)

print("\n===== STUDENT DATA =====")
print(student)


# =================================
# MAKE PREDICTION
# =================================

prediction = model.predict(student)

probability = model.predict_proba(student)

print("\n===== PREDICTION RESULT =====")

if prediction[0] == 1:
    print("Student is likely TO BE PLACED")
else:
    print("Student is likely NOT TO BE PLACED")


print("\n===== PREDICTION PROBABILITY =====")

print("Not Placed:", round(probability[0][0] * 100, 2), "%")
print("Placed:", round(probability[0][1] * 100, 2), "%")
