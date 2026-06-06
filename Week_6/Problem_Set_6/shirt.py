import sys
from PIL import Image, ImageOps


def main():
    in_file, out_file = get_user_input()
    try:
        create_overlay(in_file, out_file)
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_user_input():
    if len(sys.argv) == 3:
        in_extension = sys.argv[1].lower().split(".")[-1]
        out_extension = sys.argv[2].lower().split(".")[-1]
        if in_extension in ("jpg", "jpeg", "png"):
            if in_extension == out_extension:
                return sys.argv[1], sys.argv[2]
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def create_overlay(in_file, out_file):
    image = Image.open(in_file)
    shirt = Image.open("shirt.png")
    cropped = ImageOps.fit(image, shirt.size)
    cropped.paste(shirt, shirt)
    cropped.save(out_file)


if __name__ == "__main__":
    main()
