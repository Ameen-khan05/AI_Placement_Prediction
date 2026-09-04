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
# CAREER-SPECIFIC SKILLS
# =========================================================

CAREER_SKILLS = {

    "Software Developer": [
        "Python",
        "Java",
        "C++",
        "SQL",
        "Data Structures & Algorithms",
        "Git & GitHub"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "NumPy",
        "Pandas",
        "Statistics",
        "Data Visualization",
        "Machine Learning"
    ],

    "Machine Learning Engineer": [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow / PyTorch",
        "Git & GitHub"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Generative AI",
        "TensorFlow / PyTorch"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "SQL",
        "Git & GitHub",
        "Responsive Web Design",
        "Backend Development"
    ]
}


# =========================================================
# PRACTICE WEBSITE LINKS
# =========================================================

PRACTICE_LINKS = {

    "Python":
        "https://www.freecodecamp.org/learn/python-v9/",

    "Java":
        "https://www.w3schools.com/java/",

    "C":
        "https://www.learn-c.org/",

    "C++":
        "https://www.learncpp.com/",

    "HTML":
        "https://developer.mozilla.org/en-US/docs/Learn/HTML",

    "CSS":
        "https://developer.mozilla.org/en-US/docs/Learn/CSS",

    "JavaScript":
        "https://developer.mozilla.org/en-US/docs/Learn/JavaScript",

    "SQL":
        "https://sqlbolt.com/",

    "React":
        "https://react.dev/learn",

    "Django":
        "https://docs.djangoproject.com/en/stable/intro/tutorial01/",

    "Flask":
        "https://flask.palletsprojects.com/en/stable/tutorial/",

    "Machine Learning":
        "https://www.kaggle.com/learn/intro-to-machine-learning",

    "Data Science":
        "https://www.freecodecamp.org/learn/data-analysis-with-python/",

    "NumPy":
        "https://numpy.org/learn/",

    "Pandas":
        "https://pandas.pydata.org/docs/getting_started/intro_tutorials/",

    "Statistics":
        "https://www.khanacademy.org/math/statistics-probability",

    "Data Visualization":
        "https://www.kaggle.com/learn/data-visualization",

    "Deep Learning":
        "https://www.kaggle.com/learn/intro-to-deep-learning",

    "TensorFlow / PyTorch":
        "https://www.tensorflow.org/learn",

    "Natural Language Processing":
        "https://www.kaggle.com/learn/natural-language-processing",

    "Computer Vision":
        "https://www.kaggle.com/learn/computer-vision",

    "Generative AI":
        "https://www.kaggle.com/learn-guide/5-day-genai",

    "Data Structures & Algorithms":
        "https://www.geeksforgeeks.org/dsa/",

    "Git & GitHub":
        "https://docs.github.com/en/get-started",

    "Responsive Web Design":
        "https://www.freecodecamp.org/learn/2022/responsive-web-design/",

    "Backend Development":
        "https://developer.mozilla.org/en-US/docs/Learn/Server-side"
}


# =========================================================
# GENERAL PRACTICE LINKS
# =========================================================

GENERAL_LINKS = {

    "projects":
        "https://www.freecodecamp.org/learn/",

    "internships":
        "https://internshala.com/internships/",

    "aptitude":
        "https://www.indiabix.com/aptitude/",

    "interview":
        "https://www.hackerrank.com/interview/interview-preparation-kit",

    "problem_solving":
        "https://leetcode.com/problemset/",

    "github":
        "https://github.com/"
}


# =========================================================
# CALCULATE TECHNICAL SKILLS SCORE
# =========================================================

def calculate_skills_score(selected_skills, custom_skills):

    score = 0

    # Selected skills
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

        score += len(custom_list) * 5

    return min(score, 100)


# =========================================================
# FIND CAREER-SPECIFIC SKILLS TO PRACTICE
# =========================================================

def get_skills_to_practice(
    career_role,
    selected_skills,
    custom_skills
):

    recommended = CAREER_SKILLS.get(
        career_role,
        []
    )

    # Convert student's skills to lowercase
    student_skills = set()

    for skill in selected_skills:

        student_skills.add(
            skill.lower().strip()
        )

    # Add custom skills
    if custom_skills:

        for skill in custom_skills.split(","):

            if skill.strip():

                student_skills.add(
                    skill.strip().lower()
                )

    skills_to_practice = []

    for skill in recommended:

        if skill.lower() not in student_skills:

            skills_to_practice.append({
                "name": skill,
                "link": PRACTICE_LINKS.get(
                    skill,
                    "https://www.google.com/search?q="
                    + skill.replace(" ", "+")
                )
            })

    return skills_to_practice


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =========================================================
# ASSESSMENT PAGE
# =========================================================

@app.route("/assessment")
def assessment():

    return render_template(
        "assessment.html"
    )


# =========================================================
# PREDICTION
# =========================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # =================================================
        # STUDENT DETAILS
        # =================================================

        cgpa = float(
            request.form["cgpa"]
        )

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
        # CAREER ROLE SELECTED BY STUDENT
        # =================================================

        career_role = request.form.get(
            "career_role",
            "Not Selected"
        )


        # =================================================
        # TECHNICAL SKILLS SELECTED BY STUDENT
        # =================================================

        selected_skills = request.form.getlist(
            "technical_skills"
        )


        # =================================================
        # CUSTOM SKILLS
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
        # Your current model uses ONLY 5 features:
        #
        # 1. CGPA
        # 2. Internships
        # 3. Projects
        # 4. Aptitude Score
        # 5. Skills Score
        #
        # Attendance is NOT used.
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

        prediction = model.predict(
            input_data
        )[0]


        probabilities = model.predict_proba(
            input_data
        )[0]


        # =================================================
        # GET PLACEMENT PROBABILITY
        # =================================================

        placed_probability = 0

        for index, class_value in enumerate(
            model.classes_
        ):

            if class_value == 1:

                placed_probability = (
                    probabilities[index] * 100
                )


        placed_probability = round(
            placed_probability,
            1
        )


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


        if cgpa >= 8:

            strengths.append(
                "Excellent academic performance"
            )

        elif cgpa >= 7:

            strengths.append(
                "Good academic performance"
            )


        if skills_score >= 70:

            strengths.append(
                "Strong technical skill profile"
            )

        elif skills_score >= 50:

            strengths.append(
                "Good foundation of technical skills"
            )


        if internships >= 2:

            strengths.append(
                "Good internship experience"
            )

        elif internships == 1:

            strengths.append(
                "You have valuable internship experience"
            )


        if projects >= 3:

            strengths.append(
                "Strong practical project experience"
            )

        elif projects >= 2:

            strengths.append(
                "Good practical project experience"
            )


        if aptitude_score >= 80:

            strengths.append(
                "Excellent aptitude performance"
            )

        elif aptitude_score >= 70:

            strengths.append(
                "Good aptitude preparation"
            )


        if not strengths:

            strengths.append(
                "You have a good starting point and can improve your profile"
            )


        # =================================================
        # AREAS TO IMPROVE
        # =================================================

        improvements = []


        if cgpa < 7.5:

            improvements.append(
                "Improve academic performance"
            )


        if skills_score < 60:

            improvements.append(
                "Develop stronger technical skills"
            )


        if internships == 0:

            improvements.append(
                "Gain internship experience"
            )


        if projects < 2:

            improvements.append(
                "Build at least 2 practical projects"
            )


        if aptitude_score < 70:

            improvements.append(
                "Practice aptitude and logical reasoning"
            )


        if not improvements:

            improvements.append(
                "Continue improving your technical and interview skills"
            )


        # =================================================
        # CAREER-SPECIFIC SKILLS TO PRACTICE
        # =================================================

        skills_to_practice = get_skills_to_practice(
            career_role,
            selected_skills,
            custom_skills
        )


        # =================================================
        # PRACTICE RECOMMENDATIONS WITH DIRECT LINKS
        # =================================================

        recommendations = []


        # Projects
        if projects < 2:

            recommendations.append({
                "title": "Build Practical Projects",
                "description":
                    "Build real-world projects and add them to your portfolio and resume.",
                "link":
                    GENERAL_LINKS["projects"],
                "button":
                    "Practice Projects"
            })


        # Internship
        if internships == 0:

            recommendations.append({
                "title": "Find Internship Opportunities",
                "description":
                    "Gain practical experience through internships and industry projects.",
                "link":
                    GENERAL_LINKS["internships"],
                "button":
                    "Find Internships"
            })


        # Aptitude
        if aptitude_score < 70:

            recommendations.append({
                "title":
                    "Practice Aptitude & Logical Reasoning",
                "description":
                    "Improve quantitative aptitude, logical reasoning and placement-test skills.",
                "link":
                    GENERAL_LINKS["aptitude"],
                "button":
                    "Practice Aptitude"
            })


        # Technical interview
        recommendations.append({
            "title":
                "Technical Interview Preparation",
            "description":
                "Practice technical interview questions and prepare for placement interviews.",
            "link":
                GENERAL_LINKS["interview"],
            "button":
                "Practice Interview"
        })


        # Problem solving
        recommendations.append({
            "title":
                "Improve Problem-Solving & DSA",
            "description":
                "Solve programming problems and improve Data Structures and Algorithms.",
            "link":
                GENERAL_LINKS["problem_solving"],
            "button":
                "Solve Problems"
        })


        # GitHub
        recommendations.append({
            "title":
                "Build Your GitHub Portfolio",
            "description":
                "Upload your projects and maintain a professional coding portfolio.",
            "link":
                GENERAL_LINKS["github"],
            "button":
                "Open GitHub"
        })


        # =================================================
        # SEND EVERYTHING TO RESULT PAGE
        # =================================================

        return render_template(

            "result.html",

            result=result,

            probability=placed_probability,

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

            skills_to_practice=skills_to_practice,

            recommendations=recommendations
        )


    # =====================================================
    # ERROR HANDLING
    # =====================================================

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

                <h2>
                    Something went wrong
                </h2>

                <p>
                    {str(e)}
                </p>

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