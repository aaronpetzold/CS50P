# --- yell.py ---


# --- Manual loop with .append() ---
# Uses a for loop to convert each word to uppercase and appends to a list.
"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
"""


# --- Using map() function ---
# map(str.upper, words) applies str.upper to each word, returns an iterator.
"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()
"""


# --- List comprehension (most Pythonic) ---
# [word.upper() for word in words] creates a list of uppercase words.
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()