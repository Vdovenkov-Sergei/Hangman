from random import choice
from src.tools import wrap_str, Color, TRIES
import os


def choose_word(word_list):
    return choice(word_list).upper()


def display_person(tries, stages):
    return stages[tries]


def open_letters(ltr, original_word, hidden_word):
    for i, letter in enumerate(original_word):
        if letter == ltr:
            hidden_word[i] = ltr


def play(word, stages):
    hid_word = list(word)
    word_completion = ["_"] * len(word)
    guessed_letters, guessed_words = [], []
    cur_tr, text = 0, ""

    info = "Number of letters in the hidden word: "
    print(wrap_str(info), end="")
    print(wrap_str(f"{len(hid_word)}", Color.YELLOW))
    while True:
        if text != "":
            # Проверка на слово полностью
            if len(text) == len(hid_word):
                if text in guessed_words:
                    already = "\nYou've already tried word "
                    print(wrap_str(already), end="")
                    print(wrap_str(text, Color.CYAN), end="")
                    print(wrap_str(". It's not it!"))
                else:
                    guessed_words.append(text.upper())
                    # Проверка на ввод слова полностью
                    if text.upper() == "".join(hid_word):
                        print(wrap_str("Hooray! You win! "), end="")
                        print("\U0001F911")
                        break
                    else:
                        wrong = "\nUnfortunately, you guessed wrong! "
                        print(wrap_str(wrong) + "\U0001F618")
                        cur_tr += 1

            elif not text.isalpha() or len(text) != 1:
                print(wrap_str("\nWrong input!", Color.RED, Color.BOLD))

            elif text in guessed_letters:
                already = "\nYou've already tried letter "
                print(wrap_str(already), end="")
                print(wrap_str(text, Color.CYAN), end="")
                print(wrap_str(". It's not it!"))

            else:
                # Добавляем букву в список уже названных букв
                guessed_letters.append(text)
                if text in hid_word:  # Если буква была угадана
                    open_letters(text, hid_word, word_completion)
                    # Проверка на случай угадывания слова по одной букве
                    if word_completion == hid_word:
                        print(wrap_str("Hooray! You win! "), end="")
                        print("\U0001F911")
                        break
                    else:
                        guessed = "\nYou guessed! The letter "
                        print(wrap_str(guessed), end="")
                        print(wrap_str(text, Color.CYAN), end="")
                        print(wrap_str(" is in the word."))
                else:
                    wrong = "\nUnfortunately, you guessed wrong! "
                    print(wrap_str(wrong) + "\U0001F618")
                    cur_tr += 1

        if cur_tr == TRIES:
            break

        print()
        print(wrap_str(display_person(cur_tr, stages), Color.YELLOW, has_italic=False))
        print(wrap_str("Word: "), end="")
        print(" ".join(word_completion), Color.CYAN)

        enter = "\nEnter letter or the whole word: "
        print(wrap_str(enter) + Color.CYAN, end="")
        text = input().upper()
        print(Color.END, end="")
        os.system("cls")

    if cur_tr == TRIES:
        game_over = "\n    GAME_OVER"
        print(wrap_str(game_over, Color.RED, Color.BOLD))
        print("\n" + wrap_str(display_person(cur_tr, stages), Color.YELLOW, has_italic=False))

    print(wrap_str("Hidden word: "), end="")
    print(wrap_str(" ".join(hid_word), Color.CYAN))
