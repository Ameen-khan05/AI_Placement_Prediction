import pandas as pd

# Load the dataset
df = pd.read_csv("data/placement_data.csv")

print("===== DATASET BEFORE CLEANING =====")

print("\nShape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())
# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with the median
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

print("\n===== DATASET AFTER CLEANING =====")
print("Shape:", df.shape)
print("Missing values:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
# Save cleaned dataset
output_path = "data/placement_data_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Saved to:", output_path)

