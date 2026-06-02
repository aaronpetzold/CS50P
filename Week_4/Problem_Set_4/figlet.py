from pyfiglet import Figlet
import sys
from random import choice


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    font_name = get_argument(fonts)
    user_input = get_input()
    output = get_output(figlet, font_name, user_input)
    print(output)


def get_argument(fonts):
    if len(sys.argv) == 1:
        font_name = choice(fonts)
        return font_name
    elif len(sys.argv) == 3:
        if (sys.argv[1] in ("-f", "--font")) and (sys.argv[2] in fonts):
            font_name = sys.argv[2]
            return font_name
    else:
        sys.exit("Invalid usage")


def get_input():
    user_input = input("Input: ")
    return user_input


def get_output(figlet, font_name, user_input):
    figlet.setFont(font=font_name)
    output = figlet.renderText(user_input)
    return output


if __name__ == "__main__":
    main()
