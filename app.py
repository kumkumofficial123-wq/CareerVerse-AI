import streamlit as st
import plotly.express as px
from PyPDF2 import PdfReader

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="CareerVerse AI",
    page_icon="🚀",
    layout="wide"
)

# ----------------------------
# Helper Functions
# ----------------------------

def extract_text(pdf_file):
    try:
        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text

    except:
        return "Unable to read PDF."


def analyze_resume(text):

    skills_list = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "git",
        "github",
        "streamlit",
        "pandas",
        "numpy"
    ]

    found = []

    for skill in skills_list:

        if skill in text.lower():
            found.append(skill)

    score = min(len(found) * 10, 100)

    return score, found


def future_self(goal):

    return f"""
# 🚀 Future Self - 2030

## Career

You are now a successful **{goal}**.

## Achievements

✅ Built innovative projects

✅ Completed internships

✅ Created a strong portfolio

✅ Developed leadership skills

## Lifestyle

🌍 Working with global teams

💰 Financially independent

🎯 Continuously learning

## Message From Future You

Stay consistent.

Every project you build today creates opportunities tomorrow.
"""


def career_story(goal):

    return f"""
# 🛣 Career Journey

### 2026
Learn Python and Programming

### 2027
Build Projects

### 2028
Complete Internships

### 2029
Contribute to Open Source

### 2030
Become a successful **{goal}**
"""


def mentor_advice(role):

    mentors = {

        "Google Recruiter":
        """
### Google Recruiter Advice

• Build strong projects

• Improve DSA

• Create LinkedIn profile

• Practice mock interviews
        """,

        "AI Engineer":
        """
### AI Engineer Advice

• Learn Python

• Learn Machine Learning

• Learn Deep Learning

• Build AI Projects
        """,

        "Startup Founder":
        """
### Startup Founder Advice

• Solve real problems

• Build products

• Learn communication

• Learn teamwork
        """
    }

    return mentors.get(role)


def interview_questions(role):

    questions = {

        "Python": [
            "What is a List?",
            "What is a Tuple?",
            "Explain OOP.",
            "Difference between List and Tuple?"
        ],

        "AI": [
            "What is Machine Learning?",
            "What is Deep Learning?",
            "Explain Neural Networks.",
            "What is Overfitting?"
        ],

        "General": [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?",
            "Where do you see yourself in 5 years?"
        ]
    }

    return questions.get(role)


# ----------------------------
# Header
# ----------------------------

st.title("🚀 CareerVerse AI")

st.subheader(
    "Your Personal Career Simulation Platform"
)

st.markdown(
    "### 🌟 Build Skills. Visualize Success. Shape Your Future."
)

st.sidebar.success("CareerVerse AI v1.0")

# ----------------------------
# Menu
# ----------------------------

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "🏠 Home",
        "📄 Resume Analyzer",
        "🔮 Future Self Generator",
        "🛣 Career Story",
        "🧑‍🏫 AI Mentor",
        "🎤 Interview Simulator",
        "📊 Skill Dashboard",
        "🎯 Career Score"
    ]
)

# ----------------------------
# Home
# ----------------------------

if menu == "🏠 Home":

    st.header("Welcome to CareerVerse AI")

    st.info("""
CareerVerse AI helps students:

✅ Analyze Resume

✅ Visualize Future Career

✅ Generate Career Roadmap

✅ Learn From Mentors

✅ Practice Interviews

✅ Track Skill Growth
""")

# ----------------------------
# Resume Analyzer
# ----------------------------

elif menu == "📄 Resume Analyzer":

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        score, skills_found = analyze_resume(text)

        st.success("Resume Uploaded")

        st.metric(
            "ATS Score",
            f"{score}/100"
        )

        st.subheader("Detected Skills")

        if skills_found:

            for skill in skills_found:
                st.write("✅", skill)

        else:
            st.warning(
                "No skills detected"
            )

# ----------------------------
# Future Self
# ----------------------------

elif menu == "🔮 Future Self Generator":

    st.header("🔮 Future Self Generator")

    goal = st.text_input(
        "Enter Dream Career"
    )

    if st.button("Generate Future"):

        st.markdown(
            future_self(goal)
        )

# ----------------------------
# Career Story
# ----------------------------

elif menu == "🛣 Career Story":

    st.header("🛣 Career Story Generator")

    goal = st.text_input(
        "Career Goal"
    )

    if st.button("Generate Roadmap"):

        st.markdown(
            career_story(goal)
        )

# ----------------------------
# Mentor
# ----------------------------

elif menu == "🧑‍🏫 AI Mentor":

    st.header("🧑‍🏫 AI Mentor")

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

# ----------------------------
# Interview
# ----------------------------

elif menu == "🎤 Interview Simulator":

    st.header("🎤 Interview Simulator")

    role = st.selectbox(
        "Category",
        [
            "Python",
            "AI",
            "General"
        ]
    )

    if st.button("Generate Questions"):

        questions = interview_questions(role)

        for i, q in enumerate(
            questions,
            start=1
        ):
            st.write(
                f"{i}. {q}"
            )

# ----------------------------
# Dashboard
# ----------------------------

elif menu == "📊 Skill Dashboard":

    st.header("📊 Skill Dashboard")

    skills = {

        "Python": 85,
        "SQL": 65,
        "AI": 75,
        "Git": 90,
        "Communication": 80
    }

    fig = px.bar(
        x=list(skills.keys()),
        y=list(skills.values()),
        title="Career Readiness Dashboard"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if skills["Python"] >= 80:
        st.success(
            "🏅 Python Explorer Badge"
        )

    if skills["AI"] >= 70:
        st.success(
            "🤖 AI Enthusiast Badge"
        )

# ----------------------------
# Career Score
# ----------------------------

elif menu == "🎯 Career Score":

    st.header("🎯 Career Readiness Calculator")

    python_skill = st.slider(
        "Python",
        0,
        100,
        70
    )

    communication = st.slider(
        "Communication",
        0,
        100,
        70
    )

    projects = st.slider(
        "Projects",
        0,
        100,
        70
    )

    score = (
        python_skill
        + communication
        + projects
    ) / 3

    st.metric(
        "Career Readiness Score",
        f"{score:.0f}%"
    )

    if score >= 80:
        st.balloons()
        st.success(
            "🚀 Industry Ready!"
        )