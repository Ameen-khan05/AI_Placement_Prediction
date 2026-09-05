🎓 Student Placement Prediction

A Machine Learning-based web application that evaluates a student's academic performance, internship experience, project experience, aptitude, and technical skills to predict their placement outcome.

The system is designed to help students understand their placement readiness, identify areas for improvement, and access useful practice resources.

## 🌐 Live Deployment

Try the live application: **[Student Placement Prediction](https://ai-placement-prediction-65hm.onrender.com/
)**

📌 Project Overview

Student Placement Prediction is a Flask-based web application developed using Python and Machine Learning.

Students enter their details through an assessment form, including their CGPA, internships, projects, aptitude score, and technical skills. The system processes these inputs and uses a trained Random Forest Classifier to predict whether the student is likely to be placed.

Along with the prediction, the system provides:

Placement status
Placement probability
Student performance details
Selected technical skills
Selected career role
Strengths
Areas for improvement
Practice recommendations
Direct links to learning and practice websites
🎯 Objectives

The main objectives of the project are:

To develop a machine learning-based student placement prediction system.
To analyze important factors affecting student placement readiness.
To evaluate students based on academic and skill-related information.
To identify students' strengths and areas requiring improvement.
To provide useful practice and learning resources.
To create a simple and user-friendly web application for students.
✨ Key Features
👨‍🎓 Student Assessment

Students provide:

CGPA
Number of internships
Number of projects
Aptitude score
Technical skills
Preferred career role
💻 Technical Skills

Students can select multiple technical skills from the available options.

The system also allows students to enter additional skills that are not included in the predefined list.

Example skills:

Python
Java
C
C++
HTML
CSS
JavaScript
SQL
React
Django
Flask
Machine Learning
Data Science
🤖 Placement Prediction

The trained Machine Learning model predicts the student's placement status:

PLACED or NOT PLACED

The system also displays an estimated placement probability.

📊 Performance Analysis

The result page presents the student's assessment information, including:

CGPA
Internships
Projects
Aptitude Score
Technical Skills Score
💪 Strength Analysis

The system identifies positive aspects of the student's profile, such as:

Good academic performance
Internship experience
Project experience
Good aptitude preparation
Strong technical skill profile
📈 Areas for Improvement

The system identifies areas that the student can improve, such as:

Academic performance
Internship experience
Practical projects
Aptitude and logical reasoning
Technical skills
📚 Practice Recommendations

Students receive recommendations based on their assessment results.

The recommendations can include:

Programming practice
Aptitude practice
Technical interview preparation
Problem-solving
Data Structures and Algorithms
Practical project development
Internship opportunities

Direct links to relevant practice websites are also provided.

💼 Career Role

Students select their preferred career role during the assessment.

The selected career role is displayed on the result page.

🧠 Machine Learning

The project uses a Random Forest Classifier for placement prediction.

Model Input

The model uses five main numerical features:

CGPA
Number of Internships
Number of Projects
Aptitude Score
Technical Skills Score
Model Output
PLACED
or
NOT PLACED

The model also provides a probability associated with the placement prediction.

🛠️ Technologies Used
Technology	Purpose
Python	Backend development
Flask	Web application framework
Scikit-learn	Machine Learning
Random Forest	Placement prediction
Pandas	Data processing
NumPy	Numerical operations
Joblib	Saving and loading the trained model
HTML	Frontend structure
CSS	Website styling
📂 Project Structure
Student-Placement-Prediction/
│
├── app.py
├── train_model.py
├── model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/Student-Placement-Prediction.git

Move into the project directory:

cd Student-Placement-Prediction
2. Create a Virtual Environment
python -m venv .venv
Windows
.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install flask numpy pandas scikit-learn joblib
🤖 Train the Model

Run:

python train_model.py

This trains the Random Forest model and generates:

model.pkl
▶️ Run the Application

Start the Flask application:

python app.py

Then open your browser and visit:

http://127.0.0.1:5000
🔄 System Workflow
                Student
                   │
                   ▼
          Student Assessment
                   │
                   ▼
          Enter Student Details
                   │
                   ▼
          Select Technical Skills
                   │
                   ▼
          Select Career Role
                   │
                   ▼
          Calculate Skill Score
                   │
                   ▼
        Random Forest Classifier
                   │
                   ▼
          Placement Prediction
                   │
          ┌────────┴────────┐
          ▼                 ▼
       PLACED          NOT PLACED
          │                 │
          └────────┬────────┘
                   ▼
         Placement Probability
                   │
                   ▼
       Strengths & Improvements
                   │
                   ▼
       Practice Recommendations
                   │
                   ▼
          Direct Practice Links
📊 Student Case Study

A student can use the system by entering a profile such as:

CGPA              : 8.2
Internships       : 1
Projects          : 2
Aptitude Score    : 78%
Technical Skills  : Python, SQL, HTML, CSS
Career Role       : Software Developer

The system processes the information and generates a placement prediction along with the student's placement probability.

It also presents the student's selected skills, career role, strengths, areas for improvement, and relevant practice recommendations.

This demonstrates how the system can help students understand their current placement readiness and focus on improving their skills.

📚 Practice Resources

The system can provide direct links to useful platforms, including:

freeCodeCamp – Programming and web development
LeetCode – Coding and interview practice
GeeksforGeeks – DSA and problem solving
IndiaBix – Aptitude and logical reasoning
HackerRank – Programming and technical practice
Internshala – Internship opportunities
🎓 Project Benefits

The system can help students:

Understand their placement readiness
Identify strengths in their profile
Recognize areas that need improvement
Practice technical and aptitude skills
Develop practical projects
Prepare for technical interviews
Find relevant learning resources
🔮 Future Enhancements

Possible future improvements include:

Resume analysis
Job recommendation system
Company-specific placement prediction
Student login and profile management
Database integration
Interactive performance charts
Placement history tracking
Advanced Machine Learning models
Mobile application
Automated resume-based skill extraction
👨‍💻 Developer

Ameen Ulla Khan

BCA – 3rd Year

Govt. First Grade College, Mulbagal

📜 License

This project is developed for educational and academic purposes.

📌 Important

This project is a Machine Learning-based prediction system. Its placement prediction is an estimated result based on the factors used by the trained model and should not be considered a guarantee of actual employment.
