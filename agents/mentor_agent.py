def mentor_answer(role):

    mentors = {

        "Google Recruiter":
        """
Build projects.
Improve DSA.
Practice interviews.
Maintain LinkedIn.
""",

        "AI Engineer":
        """
Learn:
Python
Machine Learning
Deep Learning
Generative AI
""",

        "Startup Founder":
        """
Build products.
Solve real problems.
Create portfolio projects.
"""
    }

    return mentors.get(role)