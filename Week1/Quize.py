quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
        "correct_answer": "A"
    },
    {
        "question": "What is the capital of USA ?",
        "options": ["A. Delhi", "B. London", "C. Mumbai", "D. Washington, D.C."],
        "correct_answer": "D"
    },
    {
        "question": "Who is india prime minister",
        "options": ["A. Narendra Modi", "B. Rishi", "C. Yoginath", "D. Putin"],
        "correct_answer": "A"
    },
    {
        "question": "Which city is Silicon Valley of India",
        "options": ["A. Mumbai", "B. New Delhi", "C. Bangalore", "D. Hyderabad"],
        "correct_answer": "C"   
    },
    {
        "question": "WHO full form",
        "options": ["A. World Health Operation", "B. World Health Organization", "C. World Half Opp", "D. World Harror Organization"],
        "correct_answer": "B"
    }
]
def calculate_score(user_answers, correct_answers):
    score = 0
    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer == correct_answer:
            score += 1
    return score

def get_input():
    answer = input("Your answer: ").strip().upper()
    while answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        answer = input("Your answer: ").strip().upper()
    return answer

def provide_feedback(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        print()
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        print()

def display_final_score(score, total_questions):
    print(f"Your final score is {score} out of {total_questions}.")
    print()

def load_quiz():
    # This function could load questions from a file or database
    return quiz_questions

def main():
    questions = load_quiz()
    correct_answers = [q['correct_answer'] for q in questions]
    user_answers = []
    
    for question in questions:
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = get_input()
        user_answers.append(user_answer)
        provide_feedback(user_answer, question['correct_answer'])
    
    score = calculate_score(user_answers, correct_answers)
    display_final_score(score, len(questions))
    
if __name__ == "__main__":
    main()
