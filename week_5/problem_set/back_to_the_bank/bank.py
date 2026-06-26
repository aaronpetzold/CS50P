def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting[:5] == "hello":
        cash = 0
    elif greeting.startswith("h"):
        cash = 20
    else:
        cash = 100
    return cash


if __name__ == "__main__":
    main()
