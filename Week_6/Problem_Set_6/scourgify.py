import csv
import sys


def main():
    infile, outfile = get_user_input()
    try:
        with open(infile, "r") as i, open(outfile, "w", newline="") as o:
            reader = csv.DictReader(i)

            writer = csv.DictWriter(o, ["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_user_input():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            return sys.argv[1], sys.argv[2]
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
