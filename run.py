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
            "text": "How much do NASA space suits cost?",
            "choices": ["A. 12 millon dollars", "B .20 million dollars"],
            "correct_answer_index": "A",
        },
        {
            "text": "How many moons are in our solar system?",
            "choices": ["A. 100 moons", "B. 181 moons", "C.300 moons"],
            "correct_anser_index": "B",
        },
        {
            "text": "Which is the brightest planet in the night sky?",
            "choices": ["A. mars", "B. venus", "C. Neptune"],
            "correct_answer_index": "B",
        },
        {
            "text": "How long is one year on Jupiter?",
            "choices": ["A. 12 years", "B. 8 years", "C. 10 years"],
            "correct_answer_index_": "A",
        },
        {
            "text": "Which planet is closest in size to Earth?",
            "choices": ["A. Mars?", "B.Venus?", "C.Mercuary"],
            "correct_answer_index_": "B",
        },
        {
            "text": "What planet is named after the Roman god of war?",
            "choices": ["A. Saturn?", "B.venmus?", "C. Mars?"],
            "correct_answer_index_": "C",
        },
        {
            "text": "How many engines are on a space shuttle?",
            "choices": ["A. Three?", "B. Two", "C. One?"],
            "correct_answer_index_": "A",
        },
        {
            "text": "What country put a man intp sapce first?",
            "choices": ["A. Russia?", "B. USA?", "C. China?"],
            "correct_answer_index_": "A",
        },
        {
            "text": "What colour is the heat sheild facing the sun?",
            "choices": ["A. black?", "B. White?", "C. Grey?"],
            "correct_answer_index_": "B",
        },
        {
            "text": "What contributes towards space being so dark?",
            "choices": ["A. Not enough light?", "B. to big?", "C. A vacuum?"],
            "correct_answer_index_": "C",
        }
    ]


def game_intro():
    """
    Game intro function.
    Shows then user a welcome message and game instructions.
    """
    print("HELLO")
    print("COMPARE YOUR KNOWLEDGE TO THE QUESTIONS, GOOD LUCK!👾 ")


def users_name():
    """
    Function gives the user a way to add
    their name before playing the game.
    while condition (enter a minimum of four letters for a name)
    once conidition is True, loop will break, count down sequence
    (game starts).
    """

    while True:
        your_name = input("PLEASE ENTER YOUR NAME:")
        print("-----------------------------------")
        if len(your_name) < 4:
            print("ADD NO LESS THAN FOUR LETTERS!")
            continue
        return your_name


def show_next_question(question):
    """

    - Once function is called. the argument (question) from the list of
    questions (text:),
    will be displayed to the user.

    - Once function is called, for loop to iritate through choices and
    question list until
    false (no more questions to show the user)
    """
    print(question["text"])
    for choice in question["choices"]:
        print(f"{choice}")
    user_answer = input("enter answer here:") # add user the correct input a,b


def end_game(your_name):
    """
    End if game function, gives user two options,
    play again enter YES or press any key to exit game.
    game will take user_name value to display with the end game message.
    """
    print("That is the end of this game!")
    print("-----------------------------------")
    play_again = input("Enter Y to play again, or press any key to exit")
    if play_again == "y":
        main()
    else:
        print("sorry:" + your_name, "Good bye and good luck!")


def main():
    """

    - Main function to run all game functions.

    - Game_intro =
    Print users name, display game instructions,
    timer count down sequence before game starts.

    - show_next_question =
    for loop to get value from the_question list of questions.
    Then pass the value as an argument to the called function
    (show_next_question).

    - user_answer to run once question and choices have been displayed.
    user to input their answer.
    """
    game_intro()

    name = users_name()
    print(f"{name} Lets Begin!")
    timer = "5 4 3 2 1"
    for i in timer:
        print(i)
        time.sleep(0.3)

    for question in the_questions:
        show_next_question(question)

    end_game(name)


main()
