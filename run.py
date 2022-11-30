"""

    GAME NOTES
step 1. add a start game meassage.
step 2. Show game intsructions.
step 3. user to input name.
step 4. count down sequence and game starts.
step 5. show first question. needs imporving!!
step 6. show choices.
step 7. user to inout correct answer.
"""


import time

the_questions = [

        {
            "text": "🌍 Which is the densest planet in our solar system?",
            "choices": ["A.Earth", "B.Jupiter", "C.Saturn."],
            "correct_answer_index": 0,
        },
        {
            "text": "🌜 How many moons are in our solar system?",
            "choices": ["A.100 moons", "B.181 moons", "C.300 moons"],
            "correct_anser_index": 1,
        },
        {
            "text": "⭐️ Which is the brightest planet in the night sky?",
            "choices": ["A.mars", "B.Venus", "C. Neptune"],
            "correct_answer_index": 1,
        },
        {
            "text": "⏱️ How long is one year on Jupiter?",
            "choices": ["A.12 years", "B.8 years", "C.10 years"],
            "correct_answer_index_": 0,
        },
        {
            "text": "📏 Which planet is closest in size to Earth?",
            "choices": ["A.Mars", "B.Venus", "C.Mercuary"],
            "correct_answer_index_": 1,
        },
        {
            "text": "🕎 What planet is named after the Roman god of war?",
            "choices": ["A.Saturn", "B.Venmus", "C.Mars"],
            "correct_answer_index_": 2,
        },
        {
            "text": "🚀\n How many engines are on a space shuttle?",
            "choices": ["A.Three", "B.Two", "C.One"],
            "correct_answer_index_": 0,
        },
        {
            "text": "🇷🇺 What country put a man intp sapce first?",
            "choices": ["A.Russia", "B.USA", "C.China"],
            "correct_answer_index_": 0,
        },
        {
            "text": "🛡️ What colour is the heat sheild facing the sun?",
            "choices": ["A.Black", "B.White", "C.Grey"],
            "correct_answer_index_": 1,
        },
        {
            "text": "💡 What contributes towards space being so dark?",
            "choices": ["A.Not enough light", "B.To big", "C.A vacuum"],
            "correct_answer_index_": 2,
        }
    ]


def game_intro():
    """
    Game intro function.
    Shows the user a welcome message and game instructions.
    Function called in main function.
    """
    print("WELCOME TO SPACED OUT!🚀")
    print("----------------------------------------")
    print("YOUR MISSION:")
    print("-------------")
    print("COMPARE YOUR KNOWLEDGE AND ANSWER THE QUESTIONS ")
    print("READ EACH QUESTION")
    print("ANSWERING A,B OR C TO SEE HOW SMART YOU ARE")
    print("GOOD LUCK!👾")
    print("----------------------------------------")


def users_name():
    """
    Function gives the user an input method.
    User to enter their name for game to start.
    while condition (enter a minimum of four letters for a name)
    is True, loop will break, value is retured to function
    Count down sequence (game starts).
    Countdown called in main function.
    """

    while True:
        name = input("PLEASE ENTER YOUR NAME:").upper().strip()
        print("-----------------------------------")
        if len(name) < 4:
            print("❗️ ADD NO LESS THAN FOUR LETTERS!❗️")
            continue
        return name


def show_next_question(current_question):
    """

    - Once function is called. the argument (question) from the list of
    questions (text:),
    will be displayed to the user.

    - Once function is called, for loop to iritate through choices and
    question list until
    false (no more questions to show the user)
    """

    for choice in current_question["choices"]:
        print(choice)


def accept_user_answer():
    """
    Accepts user input and returns it.
    User is instructed to enter A,B or C. For to continue,
    until condition is true.
    Returns user_answer value. User_answer to call the function,
    in the main function.
    """
    while True:
        print("----------------------------------")
        users_answer = input("Add an answer here!").upper().strip()

        if users_answer not in ["A", "B", "C"]:
            print(str("❗️ Please answer A, B or C ❗️"))
            continue
        return users_answer


def check_user_answer(current_question, user_answer):
    """
    1. get correct answer.
    2. Get users answer.
    3. Validate user answer .
    """

    correct_answer = current_question["correct_answer_index"]
    answer = user_answer
    if answer == correct_answer:
        print("correct answer!")
    else:
        print(f"wrong!, the answer is: {correct_answer}")
    return


def end_game(name):
    """
    End if game function, gives user two options,
    play again enter YES or press any key to exit game.
    game will take user_name value to display with the end game message.
    """
    print("That is the end of this game!")
    print("-----------------------------------")
    play_again = input("Enter y to play again, or press any key to exit").lower()
    if play_again == "y":
        main()
    else:
        print("sorry:" + name, "Good bye and good luck!")
        print("End of mission")


def main():
    """

    - Main function to run all game functions.

    - Game_intro =
    Print users name, display game instructions,
    timer count down sequence before game starts.

    - show_next_question =
    Current question to take value of questions,
    in the get_question dictionary.
    For loop to irritate through key value ("text"), print question,
    to the user.
    show_next_question function to take current question as an argument, 
    then pass value to this function. For loop to display question choices.
    Function called in main function.
    """
    game_intro()

    name = users_name()
    print(f"{name} Lets Begin!")
    timer = "5🪐 4👾 3🛸 2🌏 1🎇"
    for i in timer:
        print(i)
        time.sleep(0.3)

    for current_question in the_questions:
        print(current_question["text"])
        show_next_question(current_question)
        user_answer = accept_user_answer()
        check_user_answer(current_question, user_answer)

    end_game(name)


main()
