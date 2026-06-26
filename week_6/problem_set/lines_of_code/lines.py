import sys


def main():
    file = get_file()
    try:
        count = get_count(file)
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_file():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            return sys.argv[1]
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def get_count(f):
    counter = 0
    with open(f, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped = line.lstrip()
            if not (line.isspace() or stripped.startswith("#")):
                counter += 1
    return counter


if __name__ == "__main__":
    main()
