import re


def main():
    print(count(input("Text: ")))


def count(s):
    words = re.findall(r"\w+", s)
    count = 0
    for word in words:
        if word.lower() == "um":
            count += 1
    return count

    # OR:
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
