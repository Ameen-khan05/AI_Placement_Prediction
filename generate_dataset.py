import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of students
n = 500

# Generate student data
data = {
    "Student_ID": range(1, n + 1),

    "CGPA": np.round(np.random.uniform(5.0, 10.0, n), 2),

    "10th_Percentage": np.round(
        np.random.uniform(50, 100, n), 2
    ),

    "12th_Percentage": np.round(
        np.random.uniform(50, 100, n), 2
    ),

    "Backlogs": np.random.randint(0, 6, n),

    "Internship": np.random.randint(0, 2, n),

    "Projects": np.random.randint(0, 5, n),

    "Technical_Skills": np.random.randint(1, 11, n),

    "Communication_Skills": np.random.randint(1, 11, n),

    "Aptitude_Score": np.random.randint(30, 101, n),

    "Attendance": np.round(
        np.random.uniform(60, 100, n), 2
    )
}

df = pd.DataFrame(data)


# Calculate a placement score
score = (
    df["CGPA"] * 8
    + df["10th_Percentage"] * 0.15
    + df["12th_Percentage"] * 0.15
    - df["Backlogs"] * 8
    + df["Internship"] * 10
    + df["Projects"] * 4
    + df["Technical_Skills"] * 2
    + df["Communication_Skills"] * 1.5
    + df["Aptitude_Score"] * 0.15
    + df["Attendance"] * 0.10
)


# Add a small amount of randomness
score += np.random.normal(0, 8, n)


# Convert score into placement result
df["Placement"] = np.where(score >= 120, "Placed", "Not Placed")


# Save dataset
file_path = "data/placement_data.csv"

df.to_csv(file_path, index=False)


print("========================================")
print(" STUDENT PLACEMENT DATASET CREATED")
print("========================================")

print(f"Total students: {len(df)}")
print(f"Dataset saved to: {file_path}")

print("\nFirst 5 records:")
print(df.head())

print("\nPlacement distribution:")
print(df["Placement"].value_counts())

print("\nDataset shape:")
print(df.shape)

print("\nDataset created successfully!")