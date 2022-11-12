"""
Step 1. add a start game meassage

"""


def game_intro():
    """
    Game intro and message
    """
    print("Hello")


def users_name():
    """
    For the user to enter there name.
    """

    while True:
        name = input("Please enter your name:")
        if len(name) < 3:
            print("Add four or more letters!")
            continue
        return name


def main():
    """
    To run all game functions
    """
    game_intro()

    name = users_name()
    print("Lets begin!")


main()
