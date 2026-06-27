# Internship Recommendation System

## Project Overview
The Internship Recommendation System is a full-stack web application that intelligently matches students with the most relevant internship opportunities based on their skills, education, and location preferences.

The system removes manual searching by using a rule-based weighted scoring algorithm to evaluate and rank internships from a structured dataset. It also provides skill gap analysis and a visual dashboard for better insights.


##  Features

1. Rule-based Internship Recommendation Engine
2. Weighted Scoring System (Skills, Education, Location)
3. Top 5 Internship Ranking System
4. Skill Gap Analysis for each internship
5. Interactive Data Visualization using Chart.js
6. Secure Resume Upload using Flask
7. Full-stack web application (Flask + Frontend)



##  Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend:** Python (Flask)
- **Visualization:** Chart.js
- **Data Format:** JSON
- **Security:** Werkzeug (secure file handling)



##  System Workflow

User Profile Input → Flask Backend → Weighted Scoring Engine → Internship Matching → Top 5 Results → Skill Gap Analysis → Visualization Dashboard



##  Core Logic (How It Works)

Each internship is evaluated using a **100-point scoring system**:

1. **Skills Match (40%)**
  - Uses Python set intersection to compare user skills with required skills

2. **Education Match (30%)**
  - Checks if user's education matches eligibility criteria

3. **Location Match (30%)**
  - Full score if location matches or internship is remote

### Skill Gap Analysis
Identifies missing skills:

python
missing_skills = set(internship_skills) - set(user_skills)


##  Project Structure

The project follows a clean separation of backend and frontend:

backend/
│
├── app.py
├── internships.json
├── requirements.txt
│
├── templates/
│ ├── about.html
│ ├── index.html
│ ├── recommendations.html
│ ├── applied.html
│
frontend/
│
├── style.css

##  How to Run the Project

### 1. Clone the repository
git clone https://github.com/Bhavna851/Internship-Recommendation-System.git

### 2. Navigate to backend folder
cd backend

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run Flask app
python app.py

### 5. Open in browser
http://127.0.0.1:5000/

##  Future Improvements

1. Add AI-based recommendation system using NLP
2. Integrate MySQL database instead of JSON
3. Resume parsing for automatic skill extraction
4. User authentication system (Login/Signup)
5. Deploy project on cloud (Render / AWS / Railway)


##  Author

Bhavna Shriwas  
B.Tech Computer Science Engineering  
Interested in Software Development & Data Science


