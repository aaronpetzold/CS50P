def main():
    x, y = get_fraction()
    output = get_output(x, y)
    print(output)


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if not (x > y or y <= 0 or x < 0):
                return x, y
        except ValueError:
            continue


def get_output(x, y):
    output = round(x / y * 100)
    if output >= 99:
        return "F"
    elif output <= 1:
        return "E"
    else:
        return f"{output}%"


if __name__ == "__main__":
    main()
