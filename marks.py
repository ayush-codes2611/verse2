from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load student data
with open("students.json", "r") as f:
    students = json.load(f)

student_dict = {student["name"]: student["marks"] for student in students}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [student_dict.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
