from flask import Flask, render_template, request
import json
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# --------- Load internships.json ----------
json_path = os.path.join(os.path.dirname(__file__), 'internships.json')
with open(json_path, 'r') as f:
    internships = json.load(f)

# --------- ALLOWED FILE CHECK ----------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# -------- SCORE CALCULATION --------
def calculate_score(user_skills, user_education, user_location, internship):
    user_skills_norm = set([s.strip().lower() for s in user_skills])
    internship_skills_norm = set([s.strip().lower() for s in internship.get('skills', [])])

    # Skill Score (40)
    if internship_skills_norm:
        matched = len(user_skills_norm.intersection(internship_skills_norm))
        skill_score = (matched / len(internship_skills_norm)) * 40
    else:
        skill_score = 0

    # Education Score (30)
    internship_edu = [e.lower().strip() for e in internship.get('education', [])]
    education_score = 30 if any(e.lower().strip() in internship_edu for e in user_education) else 0

    # Location Score (30)
    location_score = 30 if internship['location'].lower() == user_location.lower() or internship['location'].lower() == "remote" else 0

    return round(skill_score + education_score + location_score, 2)

# -------- SKILL GAP --------
def get_skill_gap(user_skills, internship_skills):
    u = set([s.lower().strip() for s in user_skills])
    i = set([s.lower().strip() for s in internship_skills])
    missing = i - u
    return [m.capitalize() for m in missing]

# ------------ ROUTES ------------------

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/form')
def form_page():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    name = request.form.get('name')
    skills = [s.strip() for s in request.form.get('skills', '').split(',') if s.strip()]

    # ---------- EDUCATION ----------
    education = [e.strip() for e in request.form.get('education', '').split(',') if e.strip()]
    education_other = request.form.get('education_other', '').strip()
    if education_other:
        education = [education_other]  # override if "Other" filled

    # ---------- LOCATION ----------
    location = request.form.get('location', '').strip()
    location_other = request.form.get('location_other', '').strip()
    if location_other:
        location = location_other  # override if "Other" filled

    # File upload
    file = request.files.get('resume')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    results = []
    for internship in internships:
        score = calculate_score(skills, education, location, internship)
        skill_gap = get_skill_gap(skills, internship.get('skills', []))

        results.append({
            "title": internship.get('title'),
            "skills": internship.get('skills', []),
            "education": internship.get('education', []),
            "location": internship.get('location', ''),
            "duration": internship.get('duration', ''),
            "internship_type": internship.get('type', ''),
            "stipend": internship.get('stipend', ''),
            "sector": internship.get('sector', 'N/A'),
            "score": score,
            "skill_gap": skill_gap
        })

    # Top 5
    results = sorted(results, key=lambda x: x['score'], reverse=True)[:5]
    best = results[0] if results else None

    return render_template('recommendations.html', best=best, results=results)

@app.route('/applied')
def applied():
    internship_title = request.args.get('title', 'Internship')
    return render_template('applied.html', title=internship_title)

# Run App
if __name__ == '__main__':
    app.run(debug=True)
