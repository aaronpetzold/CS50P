import sys
import csv
from tabulate import tabulate


def main():
    file = get_file()
    try:
        rows = get_rows(file)
        print(tabulate(rows, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_file():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return sys.argv[1]
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def get_rows(f):
    rows = []
    with open(f, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
        return rows


if __name__ == "__main__":
    main()
