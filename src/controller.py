from tools import *
from hangman import *

def greetings():
    greeting = "\nLet's play the game "
    print(wrap_str(greeting, Color.PURPLE, Color.ITALIC), end="")
    print(wrap_str("'GALLOWS'", Color.RED, Color.BOLD))

def main_loop():
    word_list = read_words()
    stages = read_person_stages()
    play(choose_word(word_list), stages)

    while True:
        question = "\nDo you want to play again? "
        agree = "YES <-> NO"
        thank = "\nThanks for playing! See you! "
        wrong = "\nDon't understand, please repeat. "

        print(wrap_str(question, Color.PURPLE, Color.ITALIC))
        print(wrap_str(agree, Color.GREEN))
        print(wrap_str("> ", Color.PURPLE) + Color.CYAN, end="")
        repeat = input().upper()
        print(Color.END, end='')
        if repeat == "YES":
            os.system('cls')
            play(choose_word(word_list), stages)
        elif repeat == "NO":
            print(wrap_str(thank, Color.PURPLE, Color.ITALIC) + '\U0001F609\n')
            break
        else:
            print(wrap_str(wrong, Color.PURPLE, Color.ITALIC) + '\U0001F644')

def main():
    greetings()
    main_loop()