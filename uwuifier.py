#! /usr/bin/env python3

# uwuifier.py

# Version 0.0.5
# Copyright (c) 2023 Endercat126
# MIT License

import sys
import random


VERSION = "0.0.5"

faces = [">.<", ":3", "^-^", "^.^", ">w<", "^.~", "~.^", ">.<", "^o^", "^_^", ">.>", "^3^", "^-^'", "^.^'", ">.<'", "^o^'", "^_^'", ">.>'", "^3^'"]

def kawaii() -> str:
    return random.choice(faces)

def uwuify(text: str) -> str:
    text = text.lower()
    text = text.replace('uwu', 'uru')
    text = text.replace('you', 'yu')
    text = text.replace('ove', 'uv')
    text = text.replace('w', 'ww')
    text = text.replace('r', 'w')
    text = text.replace('l', 'w')
    text = text.replace('y ', 'yy ')
    text = text.replace('- ', '~ ')
    text = text.replace('\\n', '\n')
    
    new_text = ""

    for sentence in text.split(". "):
        if sentence.endswith('.'):
            sentence = sentence.rstrip('.')
        
        face = random.choice(faces)
        new_text += sentence + f"! {face} "

    return new_text

if __name__ == "__main__":
    if sys.argv[1:]:
        if sys.argv[1] in ['--help', '-h']:
            print("UwUifier\n")

            print("Version " + VERSION)
            print("Definitely not made by Endercat126...\n")

            print("This is a simple tool to ruin text with UwU")
            print("Use at your own risk\n")

            print("Usage:")
            print("uwuifier [options] <text>")
            print("uwuifier -f <filename>")
            print("uwuifier <text>\n")

            print("Options:")

            print("--help -h:       Print this help message and exit")
            print("--version -v:    Print the version number")
            print("--file -f:       Use a file as input\n")

            print("This software is licensed under the permissive MIT License. A copy of the license can be found in LICENSE.md")
        elif sys.argv[1] in ['--version', '-v']:
            print("UwUifier version " + VERSION)
        elif sys.argv[1] in ['--file', '-f']:
            text = ""
            with open(sys.argv[2], "r") as f:
                text = f.read()
            print(uwuify(text))
        else:
            print(uwuify(sys.argv[1]))
    else:
        user_in = input("Enter a message:\n")

        print(uwuify(user_in))
