""" Task 6: Test Module validating user and giving marks """

import csv

def validate_user(username, password):
    """ Validate user credentials against a CSV file """
    with open('csv_files/userdata.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
        return False

def load_questions():
    """ Load questions and answers from a CSV file and make a list out of it"""
    questions = []
    with open('csv_files/questions.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append({
                'question': row['question'],
                'options': [row['option_a'], row['option_b'], row['option_c'], row['option_d']],
                'answer': row['answer']
            })
    return questions

def run_exam(questions):
    """ Run the exam and return the score """
    score = 0
    for q in questions:
        print(q['question'])
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")
        while True:
            answer = input("Your answer (1-4): ")
            if answer.isdigit() and 1 <= int(answer) <= 4:
                break
            print("Invalid input. Please try again (enter 1, 2, 3, or 4).")
        if q['options'][int(answer) - 1] == q['answer']:
            score += 1
    return score

def show_results(score, total):
    """ Print the score and percentage """
    print(f"you scored {score} out of {total}")
    percentage = (score / total) * 100
    print(f"your percantage: {percentage}%")

def main():
    """ Main function to run the test module """
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not validate_user(username, password):
            print("Invalid credentials. Try Again.")
        else:
            break

    questions = load_questions()
    score = run_exam(questions)
    show_results(score, len(questions))

if __name__ == "__main__":
    main()
