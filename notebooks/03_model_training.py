import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/placement_data_cleaned.csv")

print("===== CLEANED DATASET LOADED =====")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

# Separate input features and target
X = df.drop("Placement", axis=1)
y = df["Placement"]
# Convert target into numbers
y = y.map({
    "Placed": 1,
    "Not Placed": 0
})

print("\n===== ENCODED TARGET (y) =====")
print(y.head())

print("\n===== INPUT FEATURES (X) =====")
print(X.head())

print("\n===== TARGET (y) =====")
print(y.head())

print("\nNumber of input features:", X.shape[1])
print("Number of target values:", y.shape[0])
from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n===== DATA SPLIT =====")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
from sklearn.linear_model import LogisticRegression

# Create the model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

print("\n===== MODEL TRAINING COMPLETED =====")
print("Logistic Regression model trained successfully!")
from sklearn.metrics import accuracy_score

# Make predictions on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n===== MODEL EVALUATION =====")
print("Accuracy:", accuracy)
print("Accuracy percentage:", round(accuracy * 100, 2), "%")
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\n===== CONFUSION MATRIX =====")
print(cm)
from sklearn.metrics import classification_report

print("\n===== CLASSIFICATION REPORT =====")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Not Placed", "Placed"]
))
import joblib

# Save the trained model
joblib.dump(model, "model.pkl")

print("\n===== MODEL SAVED =====")
print("Model saved as model.pkl")
# Load the saved model
loaded_model = joblib.load("model.pkl")

print("\n===== MODEL LOADED =====")
print("Saved model loaded successfully!")