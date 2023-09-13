#! /usr/bin/env python3

# uwuifier.py

VERSION = "0.7-b"
LICENSE = "MIT"

# Copyright (c) 2023 Endercat126


# --- Imports ---
import random
import sys
import argparse
import argcomplete


# --- Data ---
# colours
class colours:
    reset = "\033[0m"
    bold = "\033[1m"
    dull = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    pink = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    bg_black = "\033[40m"
    bg_red = "\033[41m"
    bg_green = "\033[42m"
    bg_yellow = "\033[43m"
    bg_blue = "\033[44m"
    bg_pink = "\033[45m"
    bg_cyan = "\033[46m"
    bg_white = "\033[47m"


# some kawaii faces
kaomoji = [">.<", ":3", "^-^", "^.^", ">w<", "^.~", "~.^", ">.<", "^o^", "^_^", ">.>", "^3^", "^-^'", "^.^'", ">.<'", "^o^'",
           "^_^'", ">.>'", "^3^'", "(*^ω^)", "(*≧ω≦)", "(｡♥‿♥｡)", "(*´∀`)", "(°▽°)", "(╯✧▽✧)╯", "(＾◡＾)", "(⁄ ⁄•⁄ω⁄•⁄ ⁄)", "(*≧▽≦)", "(≧◡≦)"]

# some cute emojis
emojis = {
    "happy": ['😺', '😸'],
    "sad": ['😿', '😢'],
    "angry": ['😡', '😾', '👿'],
    "love": ['💖', '💕', '💝', '💘'],
    "cute": ['🌸', '⭐', '✨', '🍭', '🍪'],
    "surprise": ['😮', '🙀'],
    "sus": ['🧐', '😳', '💀']
}

# characters that will be changed
substitutions = {
    "you": "yu",
    "ove": "uv",
    "w": "ww",
    "r": "w",
    "l": "w",
    "y ": "yy ",
    "- ": "~ "
}

# words that are already cute enough!
preserve = ["uwu", "meow", "nyaa", "kawaii"]


# --- Parameters --

enable_substitutions = True
enable_kaomoji = True
enable_emojis = False
keep_case = False
debug = False

# --- Functions ---

def underline(text: str, char: str = "-") -> str:
    line = ""
    for i in range(len(text)):
        line += char

    return line

def is_spongebob(text: str) -> bool:
    for i in range(len(text)):
        if i % 2 == 0 and not text[i].isupper():
            return False
        elif i % 2 == 1 and not text[i].islower():
            return False

    return True


def to_spongebob(text: str) -> str:
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i].lower()

    return result


def print_debug(text: str, colour: str = colours.yellow, error: bool = False) -> None:
    if debug:
        if error:
            print(colours.red + "ERROR!!!\n" +
                  text.upper() + "\n!!!" + colours.reset)
        else:
            print(colour + text + colours.reset)


def replace_but_keep_case(input_text: str, old_sub: str, new_sub: str) -> str:
    case = ""
    if input_text.isupper():
        case = "upper"
    elif input_text.istitle():
        case = "title"
    elif is_spongebob(input_text):
        case = "spongebob"
    else:
        case = "lower"

    lower_text = input_text.lower()
    new_string = lower_text.replace(old_sub, new_sub)

    corrected_string = ""

    if case == "upper":
        corrected_string = new_string.upper()
    elif case == "title":
        corrected_string = new_string.title()
    elif case == "spongebob":
        corrected_string = to_spongebob(new_string)
    else:
        corrected_string = new_string

    return corrected_string


def get_sentences(input_text: str) -> list:
    sentences = []
    sentence = ""

    for char in input_text:
        sentence += char
        if char in ['.', '!', '?']:
            sentences.append(sentence.strip())
            sentence = ""
    if sentence:
        sentences.append(sentence.strip())
    return sentences


def get_kaomoji() -> str:
    return random.choice(kaomoji)


def uwuify(text: str) -> str:
    words = text.split(' ')

    print_debug(str(words), colours.green)

    new_words = []

    for word in words:
        if word.lower() in preserve:
            pass
        elif word.startswith('{') and word.strip('.!?').endswith('}'):
            word = word.replace('{', '').replace('}', '')
        else:
            if enable_substitutions:
                for sub in substitutions:
                    if keep_case:
                        word = replace_but_keep_case(word, sub, substitutions[sub])
                    else:
                        word = word.lower().replace(sub, substitutions[sub])

                    # print_debug(word, colours.blue)

        new_words.append(word)

    text = ' '.join(new_words)

    print_debug(text, colours.cyan)

    # get a list of sentences
    sentences = get_sentences(text)

    cute_sentences = []

    for sentence in sentences:
        if enable_kaomoji:
            sentence += ' ' + get_kaomoji()
            cute_sentences.append(sentence)

            print_debug(sentence)

    text = ' '.join(cute_sentences)

    print_debug("")

    return text


# --- Command Line Arguments ---

class CustomArgumentParser(argparse.ArgumentParser):
    def format_help(self):
        custom_help = ""

        custom_help += colours.bold + colours.pink + self.description + colours.blue + " v" + VERSION + colours.reset + "\n"
        custom_help += underline(self.description + " v" + VERSION) + "\n\n"

        custom_help += colours.cyan + "Options:" + colours.reset + "\n\n"

        for action in self._actions:
            line = "  "

            line += colours.green
            
            for opt in action.option_strings:
                line += opt + " "
            
            line += " " * (40 - len(str(action.option_strings)))

            line += colours.yellow
            line += action.help

            line += colours.reset
            line += "\n"

            custom_help += line

        custom_help += "\n"
        custom_help += colours.reset + "Created by Endercat126" + colours.reset + "\n"
        custom_help += colours.dull + colours.underline + "https://github.com/endercat126/uwuifier" + colours.reset + "\n\n"

        custom_help += colours.reset + "This software is licensed under the " + LICENSE + " license." + colours.reset + "\n"

        return custom_help

# --- Main ---

def cli() -> int:
    parser = CustomArgumentParser(description="UwUifier: make your text cute!")

    parser.add_argument('-s', '--enable_substitutions', type=bool, default=True, help='Enable substitutions')
    parser.add_argument('-k', '--enable_kaomoji', type=bool, default=True, help='Enable kaomoji')
    parser.add_argument('-e', '--enable_emojis', type=bool, default=False, help='Enable emojis')
    parser.add_argument('-c', '--keep_case', type=bool, default=False, help='Keep case (experimental)')
    parser.add_argument('-d', '--debug', type=bool, default=False, help='Enable debugging info')

    args = parser.parse_args()

    global enable_substitutions
    global enable_kaomoji
    global enable_emojis
    global keep_case
    global debug

    enable_substitutions = args.enable_substitutions
    enable_kaomoji = args.enable_kaomoji
    enable_emojis = args.enable_emojis
    keep_case = args.keep_case
    debug = args.debug

    text = input("Enter a message:\n" + colours.blue)
    print(colours.reset)
    print(colours.pink + uwuify(text))

    return 0


# when run as a script
if __name__ == "__main__":
    sys.exit(cli())