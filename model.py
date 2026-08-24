import joblib

# Load the trained model
model_data = joblib.load("model.pkl")

model = model_data["model"]

features = model_data["features"]


def predict_placement(student_data):

    values = [[
        student_data["cgpa"],
        student_data["attendance"],
        student_data["skills_score"],
        student_data["internships"],
        student_data["projects"],
        student_data["aptitude_score"]
    ]]

    prediction = model.predict(values)[0]

    probabilities = model.predict_proba(values)[0]

    placed_probability = probabilities[1] * 100
    not_placed_probability = probabilities[0] * 100

    return {
        "prediction": int(prediction),
        "placed_probability": round(placed_probability, 2),
        "not_placed_probability": round(
            not_placed_probability,
            2
        )
    }
