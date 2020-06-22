''' Building a Multiple Choice Quiz'''
from Question import Question
question_prompts = [
    "How many programmers does it take to change a light bulb?\n(a) Two\n(b) One\n(c) None, That's a hardware problem\n\n",
    "Whats the object-oriented way to become wealthy?\n(a) Determination\n(b) Hardwork\n(c) Inheritance\n\n",
    "Why do some people think Python scripting is offensive?\n(a) because white space matters\n(b) beause it's typeless program\n\n"
]
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score)+ "/" + str(len(questions)) + " correct")
run_test(questions)