def main():
    word = input("Enter something: ")
    print(f"Result: {shorten(word)}")


def shorten(word):
    result = ""
    for c in word:
        if not c.lower() in "aeiou":
            result += c
    return result


if __name__ == "__main__":
    main()
