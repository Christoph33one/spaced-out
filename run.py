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
    For loop in the main function to irrate through key values ("text")
    to display the current question.

    For loop to irrate through choices in the current_question
    to display chcices, key value ("choices")
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

        if users_answer not in ["A", "B", "C"]:
            print(str("❗️ Please answer A, B or C ❗️"))
            print("------------------------------")
            continue
        return users_answer


def check_user_answer(current_question, users_answer):
    """
    Passing the value of the current question and the user answer
    into the function.
    The if statement is to compare the users answer to the correct
    answer in the correct answer dictionary
    Return a bolean of true or false depending on the users answer.
    """
    if users_answer == current_question["correct_answer"]:
        print("That's correct!")
        print(current_question["infornation"])
        print("---------------")
        print("---------------")
        return True
    else:
        print("Sorry that's wrong!")
        print(current_question["infornation"])
        print("-------------")
        print("-------------")
        return False


def end_game(name):
    """
    End if game function, gives user two options,
    play again enter YES or press any key to exit game.
    game will take user_name value to display with the end game message.
    """
    print("That is the end of this game!")
    print("-----------------------------------")
    play_again = input("Enter y play again, or press any key to exit")
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
