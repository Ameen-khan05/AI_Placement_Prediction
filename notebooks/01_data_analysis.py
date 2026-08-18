import pandas as pd

# ==========================================
# DAY 3 - STUDENT PLACEMENT DATA ANALYSIS
# ==========================================

# 1. Load the dataset
file_path = "data/placement_data.csv"

df = pd.read_csv(file_path)

print("\n==========================================")
print("      STUDENT PLACEMENT DATASET")
print("==========================================")

# 2. Display first 5 records
print("\n1. FIRST 5 RECORDS")
print("------------------------------------------")
print(df.head())

# 3. Display last 5 records
print("\n2. LAST 5 RECORDS")
print("------------------------------------------")
print(df.tail())

# 4. Dataset shape
print("\n3. DATASET SHAPE")
print("------------------------------------------")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 5. Column names
print("\n4. COLUMN NAMES")
print("------------------------------------------")
for column in df.columns:
    print(column)

# 6. Data types
print("\n5. DATA TYPES")
print("------------------------------------------")
print(df.dtypes)

# 7. Dataset information
print("\n6. DATASET INFORMATION")
print("------------------------------------------")
df.info()

# 8. Statistical summary
print("\n7. STATISTICAL SUMMARY")
print("------------------------------------------")
print(df.describe())

# 9. Check missing values
print("\n8. MISSING VALUES")
print("------------------------------------------")
print(df.isnull().sum())

# 10. Check duplicate records
print("\n9. DUPLICATE RECORDS")
print("------------------------------------------")
print("Number of duplicate rows:", df.duplicated().sum())

# 11. Placement distribution
print("\n10. PLACEMENT DISTRIBUTION")
print("------------------------------------------")
print(df["Placement"].value_counts())

# 12. Placement percentage
print("\n11. PLACEMENT PERCENTAGE")
print("------------------------------------------")
print(
    df["Placement"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\n==========================================")
print("       DAY 3 ANALYSIS COMPLETED")
print("==========================================")