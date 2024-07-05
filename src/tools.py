# Класс для добавления цвета в выводимый текст
class Color:
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    ORANGE = "\033[38;5;214m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    PURPLE = "\033[38;5;141m"
    END = "\033[0m"


# Максимальное число попыток угадать слово
TRIES = 7


# Фукнция для получения массива угадываемых слов
def read_words():
    f_words = open("resources/words.txt", "r", encoding="utf-8")
    word_list = list(map(lambda x: x[:-1], f_words.readlines()))
    f_words.close()
    return word_list


# Функция для получения отрисовок игрока
def read_person_stages():
    f_person = open("resources/person.txt", "r", encoding="utf-8")
    stages, cur_stage = [], ""
    for part in f_person.readlines():
        if part == "\n":
            stages.append(cur_stage)
            cur_stage = ""
        cur_stage += part
    f_person.close()
    return stages


# Функция для получения цветного вывода текста
def wrap_str(str, color=Color.PURPLE, has_italic=True, *features):
    italic = Color.ITALIC if has_italic else ""
    return color + italic + "".join(features) + str + Color.END
