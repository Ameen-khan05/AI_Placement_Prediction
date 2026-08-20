from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        student_id = float(request.form["Student_ID"])
        cgpa = float(request.form["CGPA"])
        tenth_percentage = float(request.form["10th_Percentage"])
        twelfth_percentage = float(request.form["12th_Percentage"])
        backlogs = float(request.form["Backlogs"])
        internship = float(request.form["Internship"])
        projects = float(request.form["Projects"])
        technical_skills = float(request.form["Technical_Skills"])
        communication_skills = float(request.form["Communication_Skills"])
        aptitude_score = float(request.form["Aptitude_Score"])
        attendance = float(request.form["Attendance"])

        # Create input data in the same order used during training
        student_data = np.array([[
            student_id,
            cgpa,
            tenth_percentage,
            twelfth_percentage,
            backlogs,
            internship,
            projects,
            technical_skills,
            communication_skills,
            aptitude_score,
            attendance
        ]])

        # Prediction
        prediction = model.predict(student_data)[0]

        # Probability
        probability = model.predict_proba(student_data)[0]

        if prediction == 1:
            result = "Student is likely TO BE PLACED"
        else:
            result = "Student is likely NOT TO BE PLACED"

        not_placed_probability = round(probability[0] * 100, 2)
        placed_probability = round(probability[1] * 100, 2)

        return render_template(
            "predict.html",
            result=result,
            not_placed=not_placed_probability,
            placed=placed_probability
        )

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)
