data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        print(item["question"])
        answer = input("Your answer: ")

        if answer.strip().lower() == item["answer"].lower():
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect!")
            incorrect = incorrect + 1

            wrong_answers.append({
                "question": item["question"],
                "your_answer": answer,
                "correct_answer": item["answer"]
            })

    return correct, incorrect, wrong_answers


def show_results(correct, incorrect, wrong_answers):
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

    for item in wrong_answers:
        print("Question:", item["question"])
        print("Your answer:", item["your_answer"])
        print("Correct answer:", item["correct_answer"])


def main():
    correct, incorrect, wrong_answers = ask_questions()

    show_results(correct, incorrect, wrong_answers)

    if incorrect > 3:
        play_again = input("Do you want to play again? (yes/no): ")

        if play_again.lower() == "yes":
            main()


main()