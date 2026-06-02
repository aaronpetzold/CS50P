import inflect

p = inflect.engine()


def main():
    names = get_names()
    output(names)


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    return names


def output(names):
    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
