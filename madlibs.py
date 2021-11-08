# Code for the game.

import os
import subprocess
import platform
from file_lists import madlibs
from random import randint
import re


def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")


def choosePara():
    print("Menu: ")
    print("1. Choose Random.")
    print("2. Pick a number.")
    user_option = int(input("\n\n?: "))
    clear()

    if user_option == 1:
        choice = randint(0, 2)
    else:
        choice = int(input("Enter a number between 1 and 3:\n\n\n?: ")) - 1
    return choice


def extract_pattern(line):
    pass


def play_game(para):
    pass


if __name__ == "__main__":
    choice = choosePara()
    clear()

    madlib_file = open(
        os.path.abspath(
            os.getcwd()
        )
        + "/madlib_files/"
        + madlibs[choice], "r")

    para = madlib_file.read()
    play_game(para)

    print(para)
