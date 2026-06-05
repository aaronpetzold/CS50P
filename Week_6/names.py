# === File Writing and Reading ===

# --- Collect names in a list, then print sorted ---
# Asks for 3 names, stores them in a list, then prints each with "hello, " in alphabetical order.

names = []

for _ in range(3):
    names.append(input("What´s your name? "))

for name in sorted(names):
    print(f"hello, {name}")


# --- Write to file (manual close) ---
# Opens "names.txt" in append mode ("a"), writes the name with a newline, then closes manually.

name = input("What´s your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# --- Write to file (using 'with' statement) ---
# Same as above, but 'with' automatically closes the file, even if an error occurs.

name = input("What´s your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# --- Read all lines with readlines() ---
# Reads the entire file into a list of lines, then prints each name after removing the newline.

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())


# --- Read file by iterating directly (memory efficient) ---
# Loops over the file object line by line without storing all lines in a list.

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


# --- Read, store in list, sort in reverse, then print ---
# Reads all names into a list, sorts them in reverse order, then prints.

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")


# --- Sort lines while reading (no separate list) ---
# Sorts the lines directly from the file object and prints them.

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

















"""
names = []

for _ in range(3):
    names.append(input("What´s your name? "))

for name in sorted(names):
    print(f"hello, {name}")
"""

"""
name = input("What´s your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""


"""
name = input("What´s your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""


"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
"""


"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello," line.rstrip())
"""


"""
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
"""


"""
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
"""
