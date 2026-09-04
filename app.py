from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# =========================================================
# LOAD TRAINED MODEL
# =========================================================

model_data = joblib.load("model.pkl")
model = model_data["model"]

# =========================================================
# TECHNICAL SKILL WEIGHTS
# =========================================================

SKILL_WEIGHTS = {
    "Python": 10,
    "Java": 9,
    "C": 7,
    "C++": 8,
    "HTML": 5,
    "CSS": 5,
    "JavaScript": 8,
    "SQL": 8,
    "React": 9,
    "Django": 9,
    "Flask": 8,
    "Machine Learning": 10,
    "Data Science": 10
}


# =========================================================
# CALCULATE TECHNICAL SKILLS SCORE
# =========================================================

def calculate_skills_score(selected_skills, custom_skills):

    score = 0

    # Score for selected skills
    for skill in selected_skills:
        if skill in SKILL_WEIGHTS:
            score += SKILL_WEIGHTS[skill]

    # Score for manually entered skills
    if custom_skills:

        custom_list = [
            skill.strip()
            for skill in custom_skills.split(",")
            if skill.strip()
        ]

        # 5 points for every custom skill
        score += len(custom_list) * 5

    # Maximum score = 100
    score = min(score, 100)

    return score


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# ASSESSMENT PAGE
# =========================================================

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


# =========================================================
# PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # =================================================
        # GET STUDENT DETAILS
        # =================================================

        cgpa = float(request.form["cgpa"])

        internships = int(
            request.form["internships"]
        )

        projects = int(
            request.form["projects"]
        )

        aptitude_score = float(
            request.form["aptitude_score"]
        )

        # =================================================
        # GET CAREER ROLE SELECTED BY STUDENT
        # =================================================

        career_role = request.form.get(
            "career_role",
            "Not Selected"
        )

        # =================================================
        # GET TECHNICAL SKILLS
        # =================================================

        selected_skills = request.form.getlist(
            "technical_skills"
        )

        # =================================================
        # GET CUSTOM SKILLS
        # =================================================

        custom_skills = request.form.get(
            "custom_skills",
            ""
        )

        # =================================================
        # CALCULATE SKILLS SCORE
        # =================================================

        skills_score = calculate_skills_score(
            selected_skills,
            custom_skills
        )

        # =================================================
        # MODEL INPUT
        #
        # IMPORTANT:
        # The model uses ONLY these 5 features.
        #
        # cgpa
        # internships
        # projects
        # aptitude_score
        # skills_score
        # =================================================

        input_data = [[
            cgpa,
            internships,
            projects,
            aptitude_score,
            skills_score
        ]]

        # =================================================
        # MACHINE LEARNING PREDICTION
        # =================================================

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(
            input_data
        )[0]

        # Find probability belonging to class 1
        placed_probability = 0

        for index, class_value in enumerate(model.classes_):

            if class_value == 1:
                placed_probability = probabilities[index] * 100

        # =================================================
        # PLACEMENT RESULT
        # =================================================

        if prediction == 1:

            result = "PLACED"

        else:

            result = "NOT PLACED"

        # =================================================
        # STRENGTHS
        # =================================================

        strengths = []

        if cgpa >= 7.5:

            strengths.append(
                "Good academic performance"
            )

        if internships >= 1:

            strengths.append(
                "Internship experience"
            )

        if projects >= 2:

            strengths.append(
                "Good practical project experience"
            )

        if aptitude_score >= 70:

            strengths.append(
                "Good aptitude preparation"
            )

        if skills_score >= 60:

            strengths.append(
                "Strong technical skill profile"
            )

        if not strengths:

            strengths.append(
                "You have a good opportunity to improve your profile"
            )

        # =================================================
        # AREAS TO IMPROVE
        # =================================================

        improvements = []

        if cgpa < 7.5:

            improvements.append(
                "Improve academic performance"
            )

        if internships == 0:

            improvements.append(
                "Gain internship experience"
            )

        if projects < 2:

            improvements.append(
                "Build more practical projects"
            )

        if aptitude_score < 70:

            improvements.append(
                "Practice aptitude and logical reasoning"
            )

        if skills_score < 60:

            improvements.append(
                "Develop more technical skills"
            )

        if not improvements:

            improvements.append(
                "Continue improving your technical knowledge"
            )

        # =================================================
        # SKILLS TO PRACTICE
        # =================================================

        skills_to_practice = []

        # If student has not selected Python
        if "Python" not in selected_skills:

            skills_to_practice.append("Python")

        # SQL is useful for most software/data roles
        if "SQL" not in selected_skills:

            skills_to_practice.append("SQL")

        # JavaScript
        if "JavaScript" not in selected_skills:

            skills_to_practice.append("JavaScript")

        # Data Structures
        skills_to_practice.append(
            "Data Structures & Algorithms"
        )

        # Problem solving
        skills_to_practice.append(
            "Problem Solving"
        )

        # Interview
        skills_to_practice.append(
            "Technical Interview Preparation"
        )

        # =================================================
        # RECOMMENDATIONS
        # =================================================

        recommendations = []

        if projects < 2:

            recommendations.append(
                "Build at least 2 practical projects"
            )

        if internships == 0:

            recommendations.append(
                "Look for internship opportunities"
            )

        if aptitude_score < 70:

            recommendations.append(
                "Practice aptitude and logical reasoning regularly"
            )

        if skills_score < 60:

            recommendations.append(
                "Learn additional technical skills"
            )

        recommendations.append(
            "Practice common technical interview questions"
        )

        recommendations.append(
            "Improve problem-solving skills"
        )

        # =================================================
        # SEND DATA TO RESULT PAGE
        # =================================================

        return render_template(
            "result.html",

            result=result,

            probability=round(
                placed_probability,
                1
            ),

            cgpa=cgpa,

            internships=internships,

            projects=projects,

            aptitude_score=aptitude_score,

            skills_score=skills_score,

            selected_skills=selected_skills,

            custom_skills=custom_skills,

            # Student-selected career role
            career_role=career_role,

            strengths=strengths,

            improvements=improvements,

            skills_to_practice=skills_to_practice,

            recommendations=recommendations
        )

    except Exception as e:

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
            <style>
                body {{
                    font-family: Arial;
                    background: #f5f7fb;
                    padding: 50px;
                }}

                .error {{
                    background: white;
                    padding: 30px;
                    border-radius: 15px;
                    max-width: 700px;
                    margin: auto;
                    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                }}

                h2 {{
                    color: #dc2626;
                }}

                a {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 12px 20px;
                    background: #2563eb;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                }}
            </style>
        </head>

        <body>

            <div class="error">

                <h2>Something went wrong</h2>

                <p>{str(e)}</p>

                <a href="/assessment">
                    Go Back to Assessment
                </a>

            </div>

        </body>
        </html>
        """


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )