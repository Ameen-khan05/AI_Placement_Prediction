🎓 AI Student Placement Prediction & Career Guidance System

An AI/ML-based web application that predicts a student's placement status using academic performance, technical skills, internships, projects, and aptitude score. The system also provides placement probability, performance analysis, areas for improvement, practice recommendations, and career guidance.

My live website link:https://ai-placement-prediction-65hm.onrender.com/

📌 Project Overview

Students often find it difficult to understand their placement readiness and identify the areas they need to improve.

This project uses a Machine Learning model to analyze important student-related factors and predict whether a student is likely to be placed.

Instead of only providing a PLACED / NOT PLACED prediction, the system also analyzes the student's profile and provides personalized suggestions for improving technical skills, aptitude, projects, internships, and interview preparation.

🎯 Objectives

Predict student placement status using Machine Learning.

Provide an estimated placement probability.

Analyze the student's strengths and weak areas.

Suggest skills and topics that should be practiced.

Provide career-specific preparation recommendations.

Help students understand their placement readiness.


🚀 Features

🔮 Placement Prediction

The system predicts:

PLACED

NOT PLACED


along with the estimated placement probability.

📊 Performance Analysis

The system analyzes:

CGPA

Attendance

Skills Score

Number of Internships

Number of Projects

Aptitude Score


💪 Strength Analysis

Students can see the areas where they are performing well, such as:

Academic performance

Technical skills

Aptitude

Project experience

Industry exposure


⚠️ Improvement Areas

If a student has weaker performance in a particular area, the system identifies it and provides suggestions.

For example:

> Low Skills Score → Practice programming, problem solving and Data Structures & Algorithms.



> No Internships → Gain practical experience through internships, hackathons or real-world projects.



> Low Aptitude Score → Practice quantitative aptitude and logical reasoning.



📚 Personalized Practice Recommendations

The system recommends what the student should practice based on their profile.

💼 Career Guidance

Students can select an interested career role and receive preparation recommendations for roles such as:

Software Developer

Web Developer

Data Analyst

Data Scientist

Machine Learning Engineer

QA Engineer


🎯 Interview Preparation

The application also provides general placement interview preparation suggestions.


---

🧠 Machine Learning

The Machine Learning model uses the following features for prediction:

Feature Description

CGPA Academic performance
Attendance Attendance percentage
Skills Score Technical skill level
Internships Number of internships
Projects Number of completed projects
Aptitude Score Aptitude test performance


The trained model is saved as:

model.pkl

and is loaded by the application to make predictions for new students.


---

🏗️ System Architecture

Student
                 │
                 ▼
        Student Assessment
                 │
                 ▼
          Flask Web App
                 │
                 ▼
       Trained ML Model
          (model.pkl)
                 │
                 ▼
        Placement Prediction
                 │
        ┌────────┴────────┐
        ▼ ▼
     PLACED NOT PLACED
        │ │
        ▼ ▼
   Strengths Weak Areas
   Career Tips Practice Tips
   Interview Skill Improvement
   Preparation Recommendations
        │ │
        └────────┬────────┘
                 ▼
         Career Guidance

🛠️ Technologies Used

Programming Language

Python


Machine Learning

Scikit-learn

Pandas

NumPy


Web Development

Flask

HTML

CSS


Model Storage

Joblib


Development Environment

Visual Studio Code

Git

GitHub



---

📁 Project Structure

AI-Placement-Prediction/
│
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
│
├── data/
│ └── placement_data.csv
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/
    └── style.css


---

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Move into the project directory:

cd AI-Placement-Prediction

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

4. Install Required Libraries

pip install -r requirements.txt

If requirements.txt is not available, install the main libraries:

pip install flask pandas numpy scikit-learn joblib

5. Run the Application

python app.py

The application will start locally.

Open your browser and visit:

http://127.0.0.1:5000


---

🔄 How the Application Works

Step 1 — Enter Student Information

The student enters:

CGPA
Attendance
Skills Score
Internships
Projects
Aptitude Score

and selects an interested career role.

Step 2 — ML Prediction

The Flask application sends the input data to the trained Machine Learning model.

Step 3 — Prediction

The model predicts whether the student is:

PLACED

or

NOT PLACED

Step 4 — Probability

The application displays the estimated placement probability.

Step 5 — Career Guidance

The system analyzes the student's profile and provides:

Strengths

Weak areas

Practice recommendations

Skills to improve

Career-specific preparation

Interview preparation



---

📈 Example Output

Example 1 — Placed

Prediction: PLACED

Placement Probability: 89.5%

Strengths:
✓ Good technical skills
✓ Good project experience
✓ Strong academic performance

Example 2 — Not Placed

Prediction: NOT PLACED

Placement Probability: 38.5%

Areas to Improve:
⚠ Technical skills
⚠ Aptitude
⚠ Project experience

What You Should Practice:
• Data Structures & Algorithms
• Programming fundamentals
• Quantitative aptitude
• Logical reasoning
• Build practical projects


---

⚠️ Important Note

The placement probability is an estimate generated by the Machine Learning model based on the input features.

It does not guarantee actual placement, because real-world placement decisions can depend on many additional factors such as company requirements, interview performance, communication skills, market conditions, and eligibility criteria.


---

🔮 Future Enhancements

Possible future improvements include:

Student login and profile management

Placement history dashboard

Resume analysis

Advanced career recommendations

Company-specific placement prediction

Interactive performance charts

More Machine Learning algorithms for comparison

Database integration

Automated model retraining

Deployment on a cloud platform



---

👨‍💻 Project Purpose

This project was developed as an AI/ML internship project to demonstrate the practical implementation of:

Data preprocessing

Machine Learning

Model training

Model prediction

Flask web development

Model integration

Personalized recommendation logic

Git/GitHub version control



---

⭐ Conclusion

The AI Student Placement Prediction & Career Guidance System combines Machine Learning and web development to provide students with an estimated placement prediction and actionable career guidance.

The main goal is not only to predict "PLACED" or "NOT PLACED", but also to help students understand why they received that prediction and what they can improve.


---

