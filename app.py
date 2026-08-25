from flask import Flask, render_template, request
from model import predict_placement

app = Flask(__name__)


# ==========================================
# HOME PAGE
# ==========================================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# PREDICTION
# ==========================================
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # -------------------------------
        # Get student input
        # -------------------------------
        cgpa = float(request.form["cgpa"])
        attendance = float(request.form["attendance"])
        skills_score = float(request.form["skills_score"])
        internships = int(request.form["internships"])
        projects = int(request.form["projects"])
        aptitude_score = float(request.form["aptitude_score"])

        career_role = request.form.get(
            "career_role",
            "Software Developer"
        )

        # -------------------------------
        # Basic validation
        # -------------------------------
        if not 0 <= cgpa <= 10:
            raise ValueError("CGPA must be between 0 and 10.")

        if not 0 <= attendance <= 100:
            raise ValueError("Attendance must be between 0 and 100.")

        if not 0 <= skills_score <= 100:
            raise ValueError("Skills score must be between 0 and 100.")

        if internships < 0:
            raise ValueError("Internships cannot be negative.")

        if projects < 0:
            raise ValueError("Projects cannot be negative.")

        if not 0 <= aptitude_score <= 100:
            raise ValueError("Aptitude score must be between 0 and 100.")

        # -------------------------------
        # Student data for ML model
        # -------------------------------
        student_data = {
            "cgpa": cgpa,
            "attendance": attendance,
            "skills_score": skills_score,
            "internships": internships,
            "projects": projects,
            "aptitude_score": aptitude_score
        }

        # -------------------------------
        # ML prediction
        # -------------------------------
        result = predict_placement(student_data)

        # -------------------------------
        # Analyze student's profile
        # -------------------------------
        strengths = []
        weak_areas = []
        practice = []
        suggestions = []
        interview_tips = []

        # CGPA analysis
        if cgpa >= 8:
            strengths.append("Strong academic performance")
        elif cgpa < 7:
            weak_areas.append("Academic performance")
            practice.append(
                "Focus on improving semester scores and core subjects."
            )
        else:
            practice.append(
                "Maintain your CGPA and focus on consistent academic performance."
            )

        # Attendance analysis
        if attendance >= 85:
            strengths.append("Good attendance")
        elif attendance < 75:
            weak_areas.append("Attendance")
            practice.append(
                "Improve attendance and maintain regular participation in classes."
            )

        # Skills analysis
        if skills_score >= 75:
            strengths.append("Good technical skills")
        elif skills_score < 60:
            weak_areas.append("Technical skills")
            practice.append(
                "Practice programming fundamentals, problem solving, "
                "Data Structures and Algorithms."
            )
            suggestions.append(
                "Strengthen at least one programming language such as Python, "
                "Java or C++."
            )

        # Internship analysis
        if internships >= 1:
            strengths.append("Practical industry exposure")
        else:
            weak_areas.append("Industry experience")
            practice.append(
                "Try to gain practical experience through internships, "
                "hackathons or real-world projects."
            )

        # Project analysis
        if projects >= 2:
            strengths.append("Good project experience")
        elif projects < 2:
            weak_areas.append("Project experience")
            practice.append(
                "Build 2 or more practical projects and add them to your resume "
                "and GitHub."
            )

        # Aptitude analysis
        if aptitude_score >= 75:
            strengths.append("Good aptitude performance")
        elif aptitude_score < 60:
            weak_areas.append("Aptitude")
            practice.append(
                "Practice quantitative aptitude, logical reasoning and "
                "verbal ability regularly."
            )

        # --------------------------------
        # General recommendations
        # --------------------------------

        career_suggestions = {
            "Software Developer": [
                "Practice Data Structures and Algorithms",
                "Improve programming fundamentals",
                "Build software projects",
                "Prepare for coding interviews"
            ],

            "Web Developer": [
                "Practice HTML, CSS and JavaScript",
                "Learn a frontend framework",
                "Build responsive websites",
                "Practice REST APIs"
            ],

            "Data Analyst": [
                "Practice Python and Pandas",
                "Learn SQL",
                "Practice data visualization",
                "Work on data analysis projects"
            ],

            "Data Scientist": [
                "Strengthen Python and statistics",
                "Practice machine learning",
                "Learn Pandas and NumPy",
                "Build ML projects"
            ],

            "Machine Learning Engineer": [
                "Practice machine learning algorithms",
                "Strengthen Python",
                "Learn model evaluation",
                "Build and deploy ML projects"
            ],

            "QA Engineer": [
                "Learn software testing",
                "Practice test case creation",
                "Learn automation testing",
                "Understand SDLC and STLC"
            ]
        }

        role_suggestions = career_suggestions.get(
            career_role,
            career_suggestions["Software Developer"]
        )

        # Interview preparation
        interview_tips = [
            "Prepare a clear explanation of your projects.",
            "Practice common HR interview questions.",
            "Revise technical fundamentals.",
            "Practice aptitude and logical reasoning questions.",
            "Be prepared to explain your strengths and weaknesses."
        ]

        # If no weaknesses were found
        if not weak_areas:
            weak_areas.append(
                "No major weakness identified"
            )

        if not strengths:
            strengths.append(
                "Keep working consistently to build a stronger profile."
            )

        # --------------------------------
        # Render result
        # --------------------------------
        return render_template(
            "result.html",
            result=result,
            student=student_data,
            career_role=career_role,
            strengths=strengths,
            weak_areas=weak_areas,
            practice=practice,
            suggestions=suggestions,
            role_suggestions=role_suggestions,
            interview_tips=interview_tips
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# ==========================================
# HEALTH CHECK
# ==========================================
@app.route("/health")
def health():
    return {
        "status": "running",
        "message": "AI Placement Predictor is working"
    }


# ==========================================
# RUN APPLICATION
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)
