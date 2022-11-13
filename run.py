"""
Step 1. add a start game meassage

"""


import time

the_questions = [

    {
        "question": "How much do NASA space suits cost?",
        "choices": ["12 millon dollars", "20 million dollars"],
        "answer_index": 0,
    },

    {
        "question": "How many moons are in our solar system",
        "choices": ["100 moons", "181 moons"],
        "anser_index": 1,
    },

    {
        "question": "Which is the brightest planet in the night sky",
        "choices": ["mars", "venus"],
        "answer_index": 1,
    },

    {
        "question": "How long is one year on Jupiter",
        "choices": ["12 years", "8 years"],
        "answer_index": 0,
    }
]


def game_intro():
    """
    Game intro function.
    Shows then user a welcome message and game instructions
    """
    print("HELLO")
    print("COMPARE YOUR KNOWLEDGE TO THE QUESTIONS, GOOD LUCK!👾 ")


def users_name():
    """
    user name function gives the user a way to add
    thier name before playing the game.
    while condition (enter a minimum of three letters for a name)
    once conidition is True, loop will break (game starts)
    """

    while True:
        name = input("PLEASE ENTER YOUR NAME:")
        if len(name) < 4:
            print("ADD NO LESS THAN FOUR LETTERS!")
            continue
        return name


def show_next_question():
    """

    Function to take key (question) as an argument to retrieve value from
    dictionary of questions.
    for loop to get key value from dictionay and print only the key (questions)
    to the user.
    """
    


def main():
    """

    To run all game functions
    timer - count down sequence before game starts
    """
    game_intro()

    name = users_name()
    print(f"{name} Lets Begin!")

    timer = "5 4 3 2 1"
    for i in timer:
        print(i)
        time.sleep(0.3)


main()
