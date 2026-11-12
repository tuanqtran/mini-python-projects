import random

# List of questions
# Store the answers
# Randomly pick questions
# Ask the questions
# See if they are correct
# Keep track of the score
# Tell the user their score

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"Question {idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            score += 1
            print(f"Correct! You got {score} out of {total_questions}\n")
        else:
            print(f"Wrong. The correct answer is: {correct_answer}\n")

    print(f"You got {score} out of {total_questions}. Your total grade is: {int(score / total_questions * 100)}\n")

python_trivia_game()

