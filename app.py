import streamlit as st
import plotly.express as px
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="CareerVerse AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------
# Helper Functions
# -------------------------

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


def analyze_resume(text):

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "git",
        "github",
        "pandas",
        "numpy",
        "streamlit"
    ]

    found = []

    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)

    score = min(len(found) * 10, 100)

    return score, found


def future_self(goal):

    return f"""
## 🌟 Your Future in 2030

### Career
You are a successful **{goal}**.

### Achievements
✅ Built impactful projects

✅ Completed internships

✅ Developed leadership skills

✅ Created a strong professional network

### Lifestyle
🏠 Financially independent

🌍 Working on exciting technologies

🎯 Helping and mentoring students

### Message from Future You
Keep learning, keep building, and never stop improving.
Every small step today creates your future tomorrow.
"""


def career_story(goal):

    return f"""
# 🛣 Career Journey Roadmap

### 2026
Learn Python and Programming Fundamentals

### 2027
Build Projects and Learn Git/GitHub

### 2028
Complete Internships and Open Source Contributions

### 2029
Develop Advanced Skills and Portfolio

### 2030
Become a Successful **{goal}**
"""


def mentor_advice(role):

    mentors = {

        "Google Recruiter":
        """
### Advice from Google Recruiter

• Build strong projects

• Improve DSA

• Optimize LinkedIn profile

• Practice interviews regularly
        """,

        "AI Engineer":
        """
### Advice from AI Engineer

• Learn Python

• Machine Learning

• Deep Learning

• Generative AI

• Build real-world projects
        """,

        "Startup Founder":
        """
### Advice from Startup Founder

• Solve real problems

• Build products

• Learn business fundamentals

• Develop communication skills
        """
    }

    return mentors.get(role, "Keep learning every day.")


def interview_questions(role):

    data = {

        "Python": [
            "What is a List?",
            "What is a Tuple?",
            "Explain OOP.",
            "Difference between List and Tuple?"
        ],

        "AI": [
            "What is Machine Learning?",
            "What is Deep Learning?",
            "What is a Neural Network?",
            "What is Overfitting?"
        ],

        "General": [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?",
            "Where do you see yourself in 5 years?"
        ]
    }

    return data.get(role, data["General"])


# -------------------------
# Title
# -------------------------

st.title("🚀 CareerVerse AI")
st.subheader("Your Personal Career Simulation Platform")
st.markdown("""
### 🌟 Build Skills. Visualize Success. Shape Your Future.
""")
st.sidebar.success("CareerVerse AI v1.0")
if skills["Python"] >= 80:
    st.success("🏅 Python Explorer")

if skills["AI"] >= 70:
    st.success("🤖 AI Enthusiast")

# -------------------------
# Sidebar
# -------------------------

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "🏠 Home",
        "📄 Resume Analyzer",
        "🔮 Future Self Generator",
        "🛣 Career Story",
        "🧑‍🏫 AI Mentor",
        "🎤 Interview Simulator",
        "📊 Skill Dashboard"
    ]
)

# -------------------------
# Home
# -------------------------

if menu == "🏠 Home":

    st.header("Welcome to CareerVerse AI")

    st.info("""
CareerVerse AI helps students:

✅ Analyze Resumes

✅ Visualize Future Career

✅ Generate Career Roadmaps

✅ Get Mentor Guidance

✅ Practice Interviews

✅ Track Skills
""")

# -------------------------
# Resume Analyzer
# -------------------------

elif menu == "📄 Resume Analyzer":

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        score, skills = analyze_resume(text)

        st.success("Resume Uploaded Successfully")

        st.metric(
            "ATS Score",
            f"{score}/100"
        )

        st.subheader("Detected Skills")

        if skills:
            for skill in skills:
                st.write("✅", skill)

        else:
            st.warning("No skills detected")

# -------------------------
# Future Self
# -------------------------

elif menu == "🔮 Future Self Generator":

    st.header("🔮 Future Self Generator")

    goal = st.text_input(
        "Enter Your Dream Career"
    )

    if st.button("Generate Future"):

        st.markdown(
            future_self(goal)
        )

# -------------------------
# Career Story
# -------------------------

elif menu == "🛣 Career Story":

    st.header("🛣 Career Story Generator")

    goal = st.text_input(
        "Career Goal"
    )

    if st.button("Generate Roadmap"):

        st.markdown(
            career_story(goal)
        )

# -------------------------
# Mentor
# -------------------------

elif menu == "🧑‍🏫 AI Mentor":

    st.header("🧑‍🏫 Career Mentor")

    role = st.selectbox(
        "Choose Mentor",
        [
            "Google Recruiter",
            "AI Engineer",
            "Startup Founder"
        ]
    )

    if st.button("Get Advice"):

        st.markdown(
            mentor_advice(role)
        )

# -------------------------
# Interview
# -------------------------

elif menu == "🎤 Interview Simulator":

    st.header("🎤 Interview Simulator")

    role = st.selectbox(
        "Choose Category",
        [
            "Python",
            "AI",
            "General"
        ]
    )

    if st.button("Generate Questions"):

        questions = interview_questions(role)

        for i, q in enumerate(questions, start=1):
            st.write(f"{i}. {q}")

# -------------------------
# Dashboard
# -------------------------

elif menu == "📊 Skill Dashboard":

    st.header("📊 Skill Dashboard")

    skills = {
        "Python": 85,
        "SQL": 65,
        "AI": 70,
        "Git": 90,
        "Communication": 75
    }

    fig = px.bar(
        x=list(skills.keys()),
        y=list(skills.values()),
        labels={
            "x": "Skills",
            "y": "Score"
        },
        title="Career Readiness Dashboard"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.metric(
        "Career Readiness Score",
        "77%"
    )

    st.success("🏅 Future AI Engineer Badge Unlocked")
st.header("🎯 Career Readiness")

python_skill = st.slider("Python",0,100,70)
communication = st.slider("Communication",0,100,70)
projects = st.slider("Projects",0,100,70)

score = (python_skill + communication + projects)/3

st.metric(
    "Career Score",
    f"{score:.0f}%"
)