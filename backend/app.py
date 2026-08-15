from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# ==========================================
# PROJECT PATHS
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# ==========================================
# FLASK APP
# ==========================================

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=FRONTEND_DIR,
    static_url_path="/static"
)

CORS(app)

# ==========================================
# READ PORTFOLIO FILES
# ==========================================

def read_file(filename):

    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.exists(filepath):
        return ""

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


skills = read_file("skills.txt")
projects = read_file("projects.txt")
experience = read_file("experience.txt")
certificates = read_file("certificates.txt")
letter = read_file("letter.txt")


# ==========================================
# PORTFOLIO SEARCH
# ==========================================

def search_portfolio(query):

    query = query.lower().strip()

    # ======================================
    # SKILLS
    # ======================================

    if any(word in query for word in [
        "skill",
        "skills",
        "python",
        "sql",
        "genai",
        "generative ai",
        "rag",
        "machine learning"
    ]):

        return skills or """
My key skills include:

Python
SQL
Machine Learning
Generative AI
Prompt Engineering
RAG
AI Agents
LLM Evaluation
Context Engineering
Data Analysis
EDA
Data Visualization
Pandas
NumPy
OpenCV
Scikit-learn
Power BI
MySQL
HTML
CSS
JavaScript
"""

    # ======================================
    # PROJECTS
    # ======================================

    if any(word in query for word in [
        "project",
        "projects"
    ]):

        return projects or """
My projects include:

1. AI Portfolio RAG
2. Smart Accident Risk Classification
3. Wind Turbine Failure Prediction
4. AI-Based Road Sign Reflectivity Detection
5. Cartoon Style Facial Expression Generation
6. Crowd Patrol
"""

    # ======================================
    # EXPERIENCE
    # ======================================

    if any(word in query for word in [
        "experience",
        "internship",
        "intern",
        "work"
    ]):

        return experience or """
I completed a Data Science Internship at Ai SPRY
from October 2025 to April 2026.

I worked with Python, Data Analysis,
Machine Learning, data preprocessing,
EDA and model evaluation.
"""

    # ======================================
    # CERTIFICATES
    # ======================================

    if any(word in query for word in [
        "certificate",
        "certificates",
        "certification",
        "certifications"
    ]):

        return certificates or """
My certifications include:

Python Programming
SQL
Power BI
Advanced Excel
ML on Cloud
Data Science & Analytics
"""

    # ======================================
    # ABOUT
    # ======================================

    if any(word in query for word in [
        "about",
        "yourself",
        "who are you",
        "profile"
    ]):

        return """
I am Ananthoju Sai Kiran, an AI & ML graduate
with hands-on experience in Python,
Machine Learning, Data Analysis,
Generative AI, RAG, LLM and
Data Science with AI.
"""

    # ======================================
    # EDUCATION
    # ======================================

    if any(word in query for word in [
        "education",
        "degree",
        "btech",
        "college"
    ]):

        return """
I completed B.Tech in Computer Science Engineering
with a specialization in AI & ML.
"""

    # ======================================
    # LETTER
    # ======================================

    if any(word in query for word in [
        "letter",
        "complaint",
        "course complaint",
        "placement complaint",
        "issue",
        "request letter"
    ]):

        return letter or """
No letter information is available.
"""

    # ======================================
    # DEFAULT ANSWER
    # ======================================

    return """
I could not find specific information about that.

Try asking:

• What are your skills?
• Tell me about your projects
• What is your experience?
• What certifications do you have?
• Tell me about yourself
• What is your education?
• Tell me about my letter?
• What is my placement complaint?
"""


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# SEARCH API
# ==========================================

@app.route("/api/search", methods=["POST"])
def search():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "No data received."
            }), 400

        query = data.get("query", "").strip()

        if not query:

            return jsonify({
                "status": "error",
                "message": "Please enter a question."
            }), 400

        answer = search_portfolio(query)

        print("QUESTION:", query)
        print("ANSWER:", answer)

        return jsonify({
            "status": "success",
            "answer": answer
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# ==========================================
# DOWNLOAD RESUME
# ==========================================

@app.route("/resume")
def resume():

    return send_from_directory(
        DATA_DIR,
        "Ananthoju Saikiran4@.pdf",
        as_attachment=True
    )


# ==========================================
# DOWNLOAD STUDENT LOSS AMOUNT PDF
# ==========================================

@app.route("/student-loss-amount")
def student_loss_amount():

    return send_from_directory(
        DATA_DIR,
        "Student loss Amount.pdf",
        as_attachment=True
    )


# ==========================================
# RUN FLASK
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )