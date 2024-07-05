from src.tools import read_words, read_person_stages
from src.hangman import wrap_str, Color, play, choose_word
import os


def greetings():
    greeting = "\nLet's play the game "
    print(wrap_str(greeting), end="")
    print(wrap_str("'GALLOWS'", Color.RED, Color.BOLD))


def main():
    greetings()
    word_list = read_words()
    stages = read_person_stages()
    play(choose_word(word_list), stages)

    while True:
        question = "\nDo you want to play again? "
        agree = "YES <-> NO"
        thank = "\nThanks for playing! See you! "
        wrong = "\nDon't understand, please repeat. "

        print(wrap_str(question))
        print(wrap_str(agree, Color.GREEN))
        print(wrap_str("> ") + Color.CYAN, end="")
        repeat = input().upper()
        print(Color.END, end="")
        if repeat == "YES":
            os.system("cls")
            play(choose_word(word_list), stages)
        elif repeat == "NO":
            print(wrap_str(thank) + "\U0001F609\n")
            break
        else:
            print(wrap_str(wrong) + "\U0001F644")
