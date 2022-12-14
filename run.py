import time

from questions import the_questions


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
    print("LETS TEST YOUR SPACE KNOWLEDGE")
    print("READ EACH OF THE 10 QUESTIONS")
    print("ANSWERING A,B OR C")
    print("LETS SEE IF YOU CAN GET ALL THE QUESTIONS CORRECT!")
    print("GOOD LUCK!👾")
    print("----------------------------------------")


def users_name():
    """
    Function gives the user an input method.
    User to enter their name for game to start.
    While condition is true (enter a minimum of four letters for a name)
    or loop will continue.
    Countdown sequence (game starts).
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
    For loop in the main function to iterate through key values ("text")
    to display the current question.

    For loop to iterate through choices in the current_question
    to display choices, key value ("choices")
    """

    for choice in current_question["choices"]:
        print(choice)


def accept_user_answer():
    """
    Accepts user input and returns it if condition is true.
    (User is instructed to enter A,B or C) else continue loop.

    Then returns user_answer in the main function, once the function
    is called.
    """
    while True:
        print("----------------------------------")
        users_answer = input("Enter Answer!").upper().strip()
        print("----------------------------------")

        if users_answer not in ["A", "B", "C"]:
            print(str("❗️ Please answer A, B or C ❗️"))
            print("------------------------------")
            continue
        return users_answer


def check_user_answer(current_question, users_answer):
    """
    Passing the value of the current question and the user answer
    into the function.

    The if statement is to compare the user's answer to the correct
    answer in the correct answer dictionary.

    Return a bolean of true or false depending on the users answer.
    """
    if users_answer == current_question["correct_answer"]:
        print("That's correct!")
        print(current_question["information"])
        print("-----------------------------")
        print("-----------------------------")
        return True
    else:
        print("Sorry that's wrong!")
        print(current_question["information"])
        print("-----------------------------")
        return False


def end_game(name):
    """
    End if game function, gives user two options,
    play again enter YES or press any key to exit game.
    Game will take user_name value (name) to display with the end game message.
    """
    print("That is the end of this game!")
    print("-----------------------------------")
    play_again = input("Enter y to play again, or press any key to exit")
    if play_again == "y":
        main()
    else:
        print("Sorry:" + name, "Good bye and good luck!")
        print("End of a mission 🎇 🚀 👾 🛸 🪐")


def main():
    """
    To execute all game functions by calling each function and
    any arguments that may be in the function call.

    1. Current_question to take a question from the dictionary of questions.

    2. Show next question to take current_question and the key (text)
    from the dictionary of questions, then display a question and the choices
    (key: value).

    3.users_answer to take the user's choice and call it in the
    accept_user_answer function.

    4.local variable (correct) to call the check_user_answer function
    and increment score by 1 and to give a point for the correct answer.

    5. end_game function to take users name (name) and end the game


    """
    game_intro()

    name = users_name()
    print(f"{name} Lets Begin!")
    timer = "5🪐 4👾 3🛸 2🌏 1🎇"
    print("------------------")
    for i in timer:
        print(i)
        time.sleep(0.3)

    score = 0
    for current_question in the_questions:
        print(current_question["text"])
        show_next_question(current_question)
        users_answer = accept_user_answer()
        correct = check_user_answer(current_question, users_answer)
        if correct:
            score += 1
            print("Your score out of 10 is:", score)
            print("-------------------------------")
            print("-------------------------------")
    end_game(name)


main()
