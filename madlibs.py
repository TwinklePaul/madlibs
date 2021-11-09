# Code for the game.

import os
import subprocess
import platform
from time import sleep
from file_lists import madlibs
from random import randint
import re


def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")


def choosePara():
    print("To begin, let's pick a paragraph. Choose one of the following option: ")
    print("1. I'll let the computer decide.")
    print("2. I'll decide the number.")
    user_option = int(input("\n\n?: "))
    clear()

    if user_option == 1:
        choice = randint(0, 2)
    else:
        choice = int(input("\nEnter a number between 1 and 3:\n\n?: ")) - 1
    clear()

    return choice


def open_file(choice):
    madlib_file = open(
        os.path.abspath(
            os.getcwd()
        )
        + "/madlib_files/"
        + madlibs[choice], "r")

    return madlib_file.read()


def fill_in_the_blanks(para):
    pattern = re.compile("(.*?(__\d+__\(.*?\))[\.|\?|,|!]?[\"]?[ |\n]?)")

    for match in pattern.findall(para):
        print(match[0])
        fill_with = input("?:")
        para = para.replace(match[1], fill_with, 3)
        clear()

    return para


def play_game():
    clear()
    print("\t\t\t\t\t Welcome! to the MADLIBS game!\n\n")
    print("\t\t\t\t\tPress Enter when you are ready!!\n\n\n\n")
    print("-*-"*36)
    input()
    clear()

    choice = choosePara()

    print("All you need to do here is fill in the blanks with the appropriate type of word(s) according to the instructions given in the bracket. Do not type anything unless prompted to.")
    print("\n\n\t\t\t\t\t Let the fun commence !!")
    for _ in ("-"*36):
        print(_, flush=True, end='..')
        sleep(0.25)
    clear()

    final_story = fill_in_the_blanks(open_file(choice))

    print("Press Enter to see the final story:")
    input()
    print(final_story)
    input()
    clear()

    print("Press 'y' to restart the game:")
    choice = input()
    if choice == 'y' or choice == 'Y':
        play_game()


if __name__ == "__main__":
    play_game()
