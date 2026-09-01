import joblib


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model_data = joblib.load("model.pkl")

model = model_data["model"]

features = model_data["features"]

skills_list = model_data["skills"]


# ==========================================
# PROCESS STUDENT SKILLS
# ==========================================

def process_skills(skills_text):

    """
    Converts the student's typed skills into
    the skill features used by the ML model.
    """

    # Create all skills as 0 initially
    skill_values = {
        skill: 0
        for skill in skills_list
    }

    if not skills_text:
        return skill_values

    # Convert input to lowercase
    text = skills_text.lower()

    # Check every supported skill
    for skill in skills_list:

        skill_lower = skill.lower()

        if skill_lower in text:
            skill_values[skill] = 1

    return skill_values


# ==========================================
# PREDICT PLACEMENT
# ==========================================

def predict_placement(student_data):

    # --------------------------------------
    # Process technical skills
    # --------------------------------------

    skill_values = process_skills(
        student_data.get("technical_skills", "")
    )


    # --------------------------------------
    # Create values for ML model
    # --------------------------------------

    values = [[
        student_data["cgpa"],
        student_data["internships"],
        student_data["projects"],
        student_data["aptitude_score"]
    ]]


    # Add technical skill values
    for skill in skills_list:

        values[0].append(
            skill_values[skill]
        )


    # --------------------------------------
    # Make prediction
    # --------------------------------------

    prediction = model.predict(values)[0]


    # --------------------------------------
    # Prediction probability
    # --------------------------------------

    probabilities = model.predict_proba(values)[0]

    not_placed_probability = probabilities[0] * 100

    placed_probability = probabilities[1] * 100


    # --------------------------------------
    # Return result
    # --------------------------------------

    return {

        "prediction": int(prediction),

        "placed_probability": round(
            placed_probability,
            2
        ),

        "not_placed_probability": round(
            not_placed_probability,
            2
        )
    }
