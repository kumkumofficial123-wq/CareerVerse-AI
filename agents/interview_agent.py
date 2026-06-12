questions = {

    "Python": [
        "What is a list?",
        "What is a tuple?",
        "Explain OOP."
    ],

    "AI": [
        "What is Machine Learning?",
        "What is Deep Learning?",
        "Explain Neural Networks."
    ]
}

def get_questions(role):

    return questions.get(
        role,
        ["Tell me about yourself."]
    )
