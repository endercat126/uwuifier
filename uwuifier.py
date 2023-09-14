#! /usr/bin/env python3

# uwuifier.py

VERSION = "0.7-b2"
LICENSE = "MIT"

# Copyright (c) 2023 Endercat126


# --- Imports ---
import random
import sys
import argparse
import argcomplete
import json

import ender_ansi as ansi

# --- Data ---

# # some kawaii faces
# kaomoji = [">.<", ":3", "^-^", "^.^", ">w<", "^.~", "~.^", ">.<", "^o^", "^_^", ">.>", "^3^", "^-^'", "^.^'", ">.<'", "^o^'",
#            "^_^'", ">.>'", "^3^'", "(*^ω^)", "(*≧ω≦)", "(｡♥‿♥｡)", "(*´∀`)", "(°▽°)", "(╯✧▽✧)╯", "(＾◡＾)", "(⁄ ⁄•⁄ω⁄•⁄ ⁄)", "(*≧▽≦)", "(≧◡≦)"]

# # some cute emojis
# emojis = {
#     "happy": ['😺', '😸'],
#     "sad": ['😿', '😢'],
#     "angry": ['😡', '😾', '👿'],
#     "love": ['💖', '💕', '💝', '💘'],
#     "cute": ['🌸', '⭐', '✨', '🍭', '🍪'],
#     "surprise": ['😮', '🙀'],
#     "sus": ['🧐', '😳', '💀']
# }

# # characters that will be changed
# substitutions = {
#     "you": "yu",
#     "ove": "uv",
#     "w": "ww",
#     "r": "w",
#     "l": "w",
#     "y ": "yy ",
#     "- ": "~ "
# }

# # words that are already cute enough!
# preserve = ["uwu", "meow", "nyaa", "kawaii"]


# # --- Parameters --

# enable_substitutions = True
# enable_kaomoji = True
# enable_emojis = False
# keep_case = False
# debug = False

# --- Functions ---

def load_config():
    with open("default_config.json", "r") as f:
        config = json.load(f)
    
    global kaomoji
    kaomoji = config["kaomoji"]

    global emojis
    emojis = config["emojis"]

    global substitutions
    substitutions = config["substitutions"]

    global preserve
    preserve = config["preserve"]

    global enable_substitutions
    global enable_kaomoji
    global enable_emojis
    global keep_case
    global debug

    enable_substitutions = config["defaults"]["enable_substitutions"]
    enable_kaomoji = config["defaults"]["enable_kaomoji"]
    enable_emojis = config["defaults"]["enable_emojis"]
    keep_case = config["defaults"]["keep_case"]
    debug = config["defaults"]["debug"]

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


def print_debug(text: str, colour: str = ansi.fg.yellow, error: bool = False) -> None:
    if debug:
        if error:
            print(ansi.fg.red + "ERROR!!!\n" +
                  text.upper() + "\n!!!" + ansi.fx.reset)
        else:
            print(colour + text + ansi.fx.reset)


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

    print_debug(str(words), ansi.fg.green)

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

                    # print_debug(word, ansi.fg.blue)

        new_words.append(word)

    text = ' '.join(new_words)

    print_debug(text, ansi.fg.cyan)

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

        custom_help += ansi.fx.bold + ansi.fg.pink + self.description + ansi.fg.blue + " v" + VERSION + ansi.fx.reset + "\n"
        custom_help += underline(self.description + " v" + VERSION) + "\n\n"

        custom_help += ansi.fg.cyan + "Options:" + ansi.fx.reset + "\n\n"

        for action in self._actions:
            line = "  "

            line += ansi.fg.green
            
            for opt in action.option_strings:
                line += opt + " "
            
            line += " " * (30 - len(str(action.option_strings)))

            line += ansi.fg.yellow
            line += action.help.rstrip('//') + " " + ansi.fx.dull + get_kaomoji()

            if action.help.endswith('//'):
                line += "\n"

            line += ansi.fx.reset
            line += "\n"

            custom_help += line

        custom_help += "\n\n"
        custom_help += ansi.fg.cyan + "Tip: " + ansi.fx.dull + "put {} around a word to prevent it from being changed" + ansi.fx.reset + "\n"

        custom_help += "\n"
        custom_help += ansi.fx.reset + "Created by Endercat126" + ansi.fx.reset + "\n"
        custom_help += ansi.fx.dull + ansi.fx.underline + "https://github.com/endercat126/uwuifier" + ansi.fx.reset + "\n\n"

        custom_help += ansi.fx.reset + "This software is licensed under the " + LICENSE + " license." + ansi.fx.reset + "\n"

        return custom_help

# --- Main ---

def cli() -> int:
    load_config()

    parser = CustomArgumentParser(description="UwUifier: make your text cute!", add_help=False)

    parser.add_argument('-h', '--help', help='Show this help message and exit', action='help')
    parser.add_argument('-s', '--substitutions', help='Toggle substitutions', action='store_true')
    parser.add_argument('-k', '--kaomoji', help='Toggle kaomoji', action='store_true')
    parser.add_argument('-e', '--emojis', help='Toggle emojis', action='store_true')
    parser.add_argument('-c', '--keep_case', help='Keep case (experimental)', action='store_true')
    parser.add_argument('-d', '--debug', help='Enable debugging info//', action='store_true')
    
    parser.add_argument('-i', '--input', help='Input file', type=str)
    parser.add_argument('-o', '--output', help='Output file', type=str)

    args = parser.parse_args()

    global enable_substitutions
    global enable_kaomoji
    global enable_emojis
    global keep_case
    global debug

    enable_substitutions = not enable_substitutions if args.substitutions else enable_substitutions
    enable_kaomoji = not enable_kaomoji if args.kaomoji else enable_kaomoji
    enable_emojis = not enable_emojis if args.emojis else enable_emojis
    keep_case = not keep_case if args.keep_case else keep_case
    debug = not debug if args.debug else debug

    # text = input(ansi.fg.green + "Enter a message:\n" + ansi.fg.blue)
    # print(ansi.fx.reset)
    # print(ansi.fg.pink + uwuify(text))

    text = ""

    if args.input:
        with open(args.input, "r") as f:
            text = f.read()
    else:
        text = input(ansi.fg.green + "Enter a message:\n" + ansi.fg.blue)

    if args.output:
        with open(args.output, "w") as f:
            f.write(uwuify(text) + "\n")
    else:
        print(ansi.fg.pink + uwuify(text))

    return 0


# when run as a script
if __name__ == "__main__":
    sys.exit(cli())