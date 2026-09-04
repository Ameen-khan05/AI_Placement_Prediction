import joblib


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model_data = joblib.load("model.pkl")

model = model_data["model"]

features = model_data["features"]


# ==========================================
# PREDICT PLACEMENT
# ==========================================

def predict_placement(student_data):

    # Get student's technical skills
    technical_skills = student_data.get(
        "technical_skills",
        []
    )

    # Count the number of skills
    technical_skill_score = len(
        technical_skills
    )

    # Maximum skills used during model training
    technical_skill_score = min(
        technical_skill_score,
        13
    )

    # --------------------------------------
    # Prepare values for ML model
    # --------------------------------------

    values = [[
        student_data["cgpa"],
        student_data["internships"],
        student_data["projects"],
        student_data["aptitude_score"],
        technical_skill_score
    ]]

    # --------------------------------------
    # Prediction
    # --------------------------------------

    prediction = model.predict(values)[0]

    # --------------------------------------
    # Prediction probability
    # --------------------------------------

    probabilities = model.predict_proba(values)[0]

    placed_probability = probabilities[1] * 100

    not_placed_probability = probabilities[0] * 100

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
        ),

        "technical_skill_score":
            technical_skill_score

    }
