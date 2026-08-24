from flask import Flask, render_template, request
import pickle

from model import predict_placement

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        student_data = {
            "cgpa": float(request.form["cgpa"]),
            "attendance": float(request.form["attendance"]),
            "skills_score": float(request.form["skills_score"]),
            "internships": int(request.form["internships"]),
            "projects": int(request.form["projects"]),
            "aptitude_score": float(request.form["aptitude_score"])
        }

        result = predict_placement(student_data)

        return render_template(
            "index.html",
            result=result,
            student=student_data
        )

    except Exception:
        return render_template(
            "index.html",
            error="Please enter valid values."
        )


@app.route("/health")
def health():
    return {
        "status": "running",
        "message": "AI Placement Predictor API is working"
    }


if __name__ == "__main__":
    app.run(debug=True)
