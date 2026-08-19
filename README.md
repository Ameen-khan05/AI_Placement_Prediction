# AI Placement Prediction

## 📌 Project Description

This project uses Machine Learning to predict whether a student is likely to be placed based on their academic performance, skills, internships, projects, backlogs, and other placement-related factors.

## 🎯 Objective

The main objective of this project is to build a Machine Learning model that can predict student placement outcomes.

## 📊 Features Used

The model uses the following student features:

- Student ID
- CGPA
- 10th Percentage
- 12th Percentage
- Backlogs
- Internship
- Projects
- Technical Skills
- Communication Skills
- Aptitude Score
- Attendance

## 🤖 Machine Learning

The project includes:

- Data analysis
- Data cleaning
- Feature selection
- Model training
- Model evaluation
- Prediction

The trained model is saved using Joblib as:

`model.pkl`

## 📈 Model Performance

The model achieved approximately **87% accuracy** on the test dataset.

## 🔮 Prediction

The model can predict whether a student is:

- Likely to be Placed
- Likely Not to be Placed

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- VS Code
- Git & GitHub
## 🔮 Prediction

The trained machine learning model is used to predict whether a student is likely to be placed.

The prediction script:

- Loads the trained model from `model.pkl`
- Loads the cleaned dataset
- Selects student features
- Generates a placement prediction
- Displays the probability of being placed or not placed

### Example Prediction Output

```text
===== PREDICTION PROBABILITY =====
Not Placed: 77.81%
Placed: 22.19%

===== PREDICTION RESULT =====
Student is likely NOT TO BE PLACED

## 📂 Project Structure

```text
AI_Placement_prediction/
│
├── data/
├── notebooks/
│ ├── 01_data_analysis.py
│ ├── 02_data_cleaning.py
│ ├── 03_model_training.py
│ └── 04_prediction.py
│
├── model.pkl
├── generate_dataset.py
├── model.py
├── requirements.txt
└── README.md
```
## ▶️ How to Run

### 1. Create a virtual environment

```bash
python -m venv .venv
```
### 2. Activate the virtual environment

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the prediction script

```bash
python notebooks/04_prediction.py
```

### 5. Expected Output

The program displays the student's data, prediction probabilities, and final placement prediction.

Example:

```text
===== PREDICTION PROBABILITY =====
Not Placed: 77.81%
Placed: 22.19%

===== PREDICTION RESULT =====
Student is likely NOT TO BE PLACED
```