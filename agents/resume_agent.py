skills = [
    "python",
    "sql",
    "machine learning",
    "git",
    "github"
]

def analyze_resume(text):

    found = []

    for skill in skills:
        if skill in text.lower():
            found.append(skill)

    score = len(found) * 20

    return score, found