import validators


def main():
    print(check(input("What´s your email? ")))


def check(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
