#!/usr/bin/env python3

class fg:
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    pink = "\033[35m"
    magenta = pink
    cyan = "\033[36m"
    aqua = cyan
    white = "\033[37m"

class bg:
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    pink = "\033[45m"
    magenta = pink
    cyan = "\033[46m"
    aqua = cyan
    white = "\033[47m"

class fx:
    reset = "\033[0m"
    bold = "\033[1m"
    dull = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    strikethrough = "\033[9m"
    dim = dull
    faint = dull
    strong = bold
    invert = reverse
    inverse = reverse
    oblique = italic
    disabled = strikethrough
    linethrough = strikethrough
    crossedout = strikethrough

def demo():
    print(fg.black + "fg.black  " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.red + "fg.red    " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.blue + "fg.blue   " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.green + "fg.green  " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.yellow + "fg.yellow " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.cyan + "fg.cyan   " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.pink + "fg.pink   " + "        " + fx.dull + "+ dull" + fx.reset)
    print(fg.white + "fg.white  " + "        " + fx.dull + "+ dull" + fx.reset)
    print()
    print(bg.black + "bg.black  " + fx.reset + "        " + bg.black + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.red + "bg.red    " + fx.reset + "        " + fg.black + bg.red + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.blue + "bg.blue   " + fx.reset + "        " + fg.black + bg.blue + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.green + "bg.green  " + fx.reset + "        " + fg.black + bg.green + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.yellow + "bg.yellow " + fx.reset + "        " + fg.black + bg.yellow + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.cyan + "bg.cyan   " + fx.reset + "        " + fg.black + bg.cyan + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.pink + "bg.pink   " + fx.reset + "        " + fg.black + bg.pink + fx.dull + "+ dull" + fx.reset)
    print(fg.black + bg.white + "bg.white  " + fx.reset + "        " + fg.black + bg.white + fx.dull + "+ dull" + fx.reset)

if __name__ == "__main__":
    demo()