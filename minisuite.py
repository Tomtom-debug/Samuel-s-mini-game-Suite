import random
def main():
    while True:
        print("\nWelcome to Samuel's Mini Game Suite")
        print("Don't forget to have fun!!" )
        print("1. Partner Matching Game")
        print("2. Best Brain Quiz")
        print("3. Exit")
        a=['1','2','3']
        choice = input("Choose a game (1-3): ")

        if choice == "1":
            game = PartnerMatchingGame()
            game.play_game()
        elif choice == "2":
            Best_brain()
        elif choice == "3":
            break
        else:
            print("Please enter a valid choice")
            main()

class PartnerMatchingGame:
    def __init__(self):
        self.couple_a_answers = {}
        self.couple_b_answers = {}

    def get_answers_from_couple_a(self):
        print("Couple A, please provide your answers:")
        questions = [
            "What is your partner's favorite color?",
            "What is your partner's dream vacation destination?",
            "What is your partner's favorite movie or TV show?",
            "What is your partner's go-to comfort food?",
            "Who is your partner's celebrity crush?",
            "What is your partner's idea of a perfect date night?",
            "What is your partner's favorite hobby or pastime?",
            "If your partner could have any superpower, what would it be?",
            "What is your partner's most cherished childhood memory?",
            "What is your partner's pet peeve or biggest annoyance?"
        ]
        for i, question in enumerate(questions, 1):
            answer = input(f"Question {i}: {question} - Answer: ")
            self.couple_a_answers[question] = answer
        print("Answers from Couple A have been recorded.\n")

    def get_answers_from_couple_b(self):
        print("Couple B, it's your turn to guess Couple A's answers:")
        correct_answers = 0
        questions = [
            "What is your partner's favorite color?",
            "What is your partner's dream vacation destination?",
            "What is your partner's favorite movie or TV show?",
            "What is your partner's go-to comfort food?",
            "Who is your partner's celebrity crush?",
            "What is your partner's idea of a perfect date night?",
            "What is your partner's favorite hobby or pastime?",
            "If your partner could have any superpower, what would it be?",
            "What is your partner's most cherished childhood memory?",
            "What is your partner's pet peeve or biggest annoyance?"
        ]
        for i, question in enumerate(questions, 1):
            guess = input(f"Question {i}: {question} - Guess the answer: ")
            if guess.lower() == self.couple_a_answers[question].lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Opps!! Wrong answer. The correct answer is: {self.couple_a_answers[question]}")
        print(f"\nCouple B, you got {correct_answers} out of 10 answers correct.")
        compatibility_percentage = (correct_answers / 10) * 100
        print(f"You are {compatibility_percentage}% compatible")
        if compatibility_percentage >= 80 :
            print("Purrr!! You guys are a great fit.")
        elif (compatibility_percentage >= 70) and (compatibility_percentage < 80):
            print("You are a good pair. You can try to work things out.")
        else:
            ("Sorry you might not be a perfect fit.")

    def play_game(self):
        self.get_answers_from_couple_a()
        self.get_answers_from_couple_b()


def Best_brain():
    score = 0
    questions = [
        {"question": "What's the capital of France?", "answer": "paris"},
        {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "In which year did Christopher Columbus discover America?", "answer": "1492"},
        {"question": "What is the square root of 16?", "answer": "4"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
        {"question": "What is the largest mammal in the world?", "answer": "blue whale"},
        {"question": "What is the symbol for the element gold?", "answer": "au"},
        {"question": "In which country was the game of chess invented?", "answer": "india"},
        {"question": "Who is the first President of the United States?", "answer": "washington"},
        {"question": "What is the formula for the area of a rectangle? (length,width)", "answer": "length x width"},
        {"question": "What is the chemical symbol for oxygen?", "answer": "o"},
        {"question": "Who painted the Mona Lisa?", "answer": "da vinci"},
        {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "What is the square of 9?", "answer": "81"},
        {"question": "What is the capital of Japan?", "answer": "tokyo"},
        {"question": "Who is known as the father of modern physics?", "answer": "einstein"},
        {"question": "Which gas do plants absorb from the atmosphere?", "answer": "carbon dioxide"},
        {"question": "Who is the author of 'To Kill a Mockingbird'?", "answer": "harper lee"},
        {"question": "What is the boiling point of water in degrees Celsius?", "answer": "100"},
        {"question": "What is the largest desert in the world?", "answer": "sahara"},
        {"question": "Who wrote 'The Great Gatsby'?", "answer": "fitzgerald"},
        {"question": "What is the chemical symbol for iron?", "answer": "fe"},
        {"question": "In which year was the Declaration of Independence adopted?", "answer": "1776"},
        {"question": "What is the smallest planet in our solar system?", "answer": "mercury"},
    ]
    random.shuffle(questions)
    for q in questions[:10]:
        print(q["question"])
        user_answer = input("Your answer: ").lower()

        if user_answer == q["answer"]:
            print("Good job. You had it Correct!")
            score += 1
        else:
            print(f"Sorry, the right answer is: {q['answer']}")
    score = (score / 10) * 100

    print(f"You scored {score}%.")
    print("Well done. You are a genius for trying")
    survey=input("I hope you had fun? ").lower()
    if survey == "Yes".lower():
        print("Thank you")
        input("Please rate this quiz program over 10 (1-10): ")
        print("Hope to see you play again soon")
    else:
        input("Please rate this quiz program over 10 (1-10): ")
        print("I hope you have fun next time")
        print("Bye!!")



if __name__ == "__main__":
    main()
