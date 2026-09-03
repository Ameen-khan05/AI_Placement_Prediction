from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# =========================================================
# LOAD MODEL
# =========================================================

model_data = joblib.load("model.pkl")
model = model_data["model"]


# =========================================================
# SKILL WEIGHTS
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

    # Predefined skills
    for skill in selected_skills:
        if skill in SKILL_WEIGHTS:
            score += SKILL_WEIGHTS[skill]

    # Custom skills
    if custom_skills:

        custom_list = [
            skill.strip()
            for skill in custom_skills.split(",")
            if skill.strip()
        ]

        # 5 points for each custom skill
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
# PREDICT
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
        # GET CAREER ROLE
        # =================================================
        # Student selects this in the assessment page.

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
        # =================================================
        # Attendance is completely removed.
        #
        # Model inputs:
        # CGPA
        # Internships
        # Projects
        # Aptitude Score
        # Technical Skills Score

        input_data = [[
            cgpa,
            internships,
            projects,
            aptitude_score,
            skills_score
        ]]


        # =================================================
        # PREDICTION
        # =================================================

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(
            input_data
        )[0]


        # =================================================
        # PLACEMENT PROBABILITY
        # =================================================

        placed_probability = probabilities[1] * 100


        # =================================================
        # RESULT
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
                "Internship experience is valuable"
            )


        if projects >= 2:
            strengths.append(
                "Good project experience"
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
                "Good opportunity to improve your profile"
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
                "Build 2 or more practical projects"
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
        # PRACTICE RECOMMENDATIONS
        # =================================================

        recommendations = []


        if skills_score < 60:
            recommendations.append(
                "Learn one additional programming technology"
            )


        if projects < 2:
            recommendations.append(
                "Build 2 or more practical projects"
            )


        if internships == 0:
            recommendations.append(
                "Look for internship opportunities"
            )


        recommendations.append(
            "Practice common interview questions"
        )


        recommendations.append(
            "Improve problem-solving and Data Structures"
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

            career_role=career_role,

            strengths=strengths,

            improvements=improvements,

            recommendations=recommendations
        )


    except Exception as e:

        return f"""
        <h2>Error</h2>

        <p>{str(e)}</p>

        <a href="/assessment">
            Go Back
        </a>
        """


# =========================================================
# ASSESSMENT PAGE
# =========================================================

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
