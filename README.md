````markdown
# 🎓 AI Student Placement Prediction & Career Guidance System

An AI/ML-based web application that predicts a student's placement status based on academic performance, internships, projects, aptitude score, and technical skills.

The system also provides personalized improvement suggestions and practice resources with direct links to useful websites.

---
---

## 🌐 Live Deployment

Try the live application: **[AI Placement Prediction](https://ai-placement-prediction-65hm.onrender.com/
)**

---

## 🚀 Project Overview

The **AI Student Placement Prediction & Career Guidance System** is designed to help students understand their placement readiness.

Students enter their academic and professional details, select their technical skills, and choose their preferred career role.

The system then:

- 🤖 Predicts placement status
- 📊 Calculates placement probability
- 💻 Analyzes technical skills
- 💼 Displays the selected career role
- 💪 Shows student strengths
- 📈 Identifies areas for improvement
- 📚 Provides practice recommendations
- 🔗 Provides direct links to practice websites

---

## ✨ Features

### 👨‍🎓 Student Assessment

Students provide:

- CGPA
- Number of internships
- Number of projects
- Aptitude score
- Technical skills

### 💻 Technical Skills

Students can select multiple technical skills such as:

- Python
- Java
- C
- C++
- HTML
- CSS
- JavaScript
- SQL
- React
- Django
- Flask
- Machine Learning
- Data Science

Students can also enter additional skills manually.

### 💼 Career Role

The student selects their preferred career role from the available options.

The system displays the **career role selected by the student** rather than automatically generating a career recommendation.

### 🤖 Placement Prediction

The machine learning model predicts:

- **PLACED**
- **NOT PLACED**

It also displays the estimated placement probability.

### 📊 Performance Analysis

The result page displays:

- CGPA
- Internships
- Projects
- Aptitude Score
- Technical Skills Score

### 💪 Strength Analysis

The system identifies areas where the student is performing well.

Example:

> Good academic performance

> Internship experience is valuable

> Good project experience

> Strong technical skill profile

### 📈 Improvement Areas

The system identifies areas that need improvement.

For example:

- Improve academic performance
- Gain internship experience
- Build practical projects
- Practice aptitude
- Develop additional technical skills

### 📚 Practice Recommendations

The system provides useful practice resources with direct links.

Examples include:

- Programming practice
- Aptitude practice
- Technical interview preparation
- Problem-solving
- Data Structures and Algorithms
- Project development
- Internship opportunities

---

# 🧠 Machine Learning Model

The project uses a **Random Forest Classifier** for placement prediction.

### Input Features

The model uses:

```text
CGPA
Internships
Projects
Aptitude Score
Technical Skills Score
````

### Output

```text
PLACED
or
NOT PLACED
```

The model also calculates the probability of placement.

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Web Framework

* Flask

### Machine Learning

* Scikit-learn
* Random Forest Classifier

### Data Processing

* Pandas
* NumPy

### Model Storage

* Joblib

### Frontend

* HTML
* CSS

### Development Environment

* Visual Studio Code

---

# 📁 Project Structure

```text
AI_Placement_prediction/
│
├── app.py
├── model.py
├── train_model.py
├── model.pkl
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── assessment.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── data/
│
├── notebooks/
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI_Placement_prediction.git
```

Move into the project folder:

```bash
cd AI_Placement_prediction
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

---

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the libraries manually:

```bash
pip install flask numpy pandas scikit-learn joblib
```

---

# 🤖 Train the Machine Learning Model

Run:

```bash
python train_model.py
```

This will train the Random Forest model and create:

```text
model.pkl
```

---

# ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

You should see something similar to:

```text
Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🔄 How the System Works

```text
Student
   ↓
Student Assessment
   ↓
Enter Academic Details
   ↓
Select Technical Skills
   ↓
Select Career Role
   ↓
Submit Assessment
   ↓
Machine Learning Model
   ↓
Placement Prediction
   ↓
Performance Analysis
   ↓
Strengths & Improvements
   ↓
Practice Recommendations
   ↓
Direct Practice Resources
```

---

# 📊 Example

A student enters:

```text
CGPA              : 8.2
Internships       : 1
Projects          : 2
Aptitude Score    : 78
Technical Skills  : Python, SQL, HTML
Career Role       : Software Developer
```

The system generates a result containing:

```text
Placement Status
Placement Probability
Performance Analysis
Technical Skills
Selected Career Role
Strengths
Areas to Improve
Practice Recommendations
```

---

# 📚 Practice Resources

The application can provide direct practice resources such as:

| Area                  | Resource      |
| --------------------- | ------------- |
| Programming           | freeCodeCamp  |
| Coding Problems       | LeetCode      |
| DSA & Problem Solving | GeeksforGeeks |
| Aptitude              | IndiaBix      |
| Coding Practice       | HackerRank    |
| Internships           | Internshala   |

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Predict student placement status using machine learning.
2. Analyze academic and technical performance.
3. Help students identify their strengths.
4. Identify areas that require improvement.
5. Provide useful practice resources.
6. Help students prepare for placement opportunities.
7. Provide an easy-to-use web-based interface.

---

# 🔮 Future Enhancements

The project can be further improved by adding:

* 📄 Resume analysis
* 🎯 Job recommendations
* 🏢 Company-specific placement prediction
* 🧠 Advanced machine learning models
* 📊 Interactive performance charts
* 🔐 Student login system
* 💾 Student profile storage
* 📧 Email-based result sharing
* 📱 Mobile-responsive improvements
* 📈 Placement analytics dashboard

---

# 👨‍💻 Developed By

**Ameen Ulla Khan**

BCA – 3rd Year

Govt. First Grade College, Mulbagal

---
