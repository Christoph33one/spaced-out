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
            "choices": ["12 millon dollars", "20 million dollars"],
            "answer_index": 0,
        },

        {
            "text": "How many moons are in our solar system?",
            "choices": ["100 moons", "181 moons"],
            "anser_index": 1,
        },

        {
            "text": "Which is the brightest planet in the night sky?",
            "choices": ["mars", "venus"],
            "answer_index": 1,
        },

        {
            "text": "How long is one year on Jupiter?",
            "choices": ["12 years", "8 years"],
            "answer_index": 0,
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
        name = input("PLEASE ENTER YOUR NAME:")
        if len(name) < 4:
            print("ADD NO LESS THAN FOUR LETTERS!")
            continue
        return name


def show_next_question(question):
    """

    - Once function is called. the argument (question) from the list of 
    questions (text:),
    will be displayed to the user.

    - Once function is called, for loop to iritate through choices and 
    question list until
    false (no more questions to show the user)
    """

    index = 1  # needs more input and questionsing!!
    print(index, question["text"])
    index += 1  # ???
    for choice in question["choices"]:  # why for loop here and not main?
        print(choice)


def grade_user_answer():
    """
    To take user answer and increment True or False
    """


grade_user_answer()


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

    for question in the_questions:  # why for loop here?
        show_next_question(question)

    users_answer = input("Add your answers here!")
    print("-------------------------------------")

main()
