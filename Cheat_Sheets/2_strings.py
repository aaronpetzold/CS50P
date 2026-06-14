# === Strings ===


# ========== TABLE OF CONTENTS ==========
#
# 1. CREATING STRINGS
# 2. STRING METHODS (CASE & WHITESPACE)
# 3. SEARCHING & CHECKING
# 4. SLICING & INDEXING
# 5. FORMATTING (f-strings, .format(), %)
# 6. ADDITIONAL USEFUL METHODS
#
# ========================================


# Definition: Strings are immutable sequences of characters.


# ---------- 1. CREATING STRINGS ----------

text = "  Hello World!  "
single = 'Hello'
multi = """This is
a multi-line string"""


# ---------- 2. STRING METHODS (CASE & WHITESPACE) ----------

# strip() - removes leading/trailing whitespace
clean = text.strip()                    # "Hello World!"

# lstrip() / rstrip() - remove only left or right
left_clean = text.lstrip()              # "Hello World!  "
right_clean = text.rstrip()             # "  Hello World!"

# lower() / upper() - change case
lower = text.lower()                    # "  hello world!  "
upper = text.upper()                    # "  HELLO WORLD!  "

# capitalize() - first letter uppercase, rest lowercase
cap = "hello world".capitalize()        # "Hello world"

# title() - first letter of each word uppercase
title = "hello world".title()           # "Hello World"

# swapcase() - swaps case of each letter
swapped = "Hello World".swapcase()      # "hELLO wORLD"

# replace() - substitutes substrings
replaced = text.replace("World", "Python")  # "  Hello Python!  "

# split() - divides into list at each separator
words = text.split()                    # ["Hello", "World!"]
words_custom = text.split("o")          # ["  Hell", " W", "rld!  "]

# splitlines() - splits at line breaks
lines = "Line1\nLine2".splitlines()     # ["Line1", "Line2"]

# join() - combines list elements with a separator
joined = "-".join(["a", "b", "c"])      # "a-b-c"


# ---------- 3. SEARCHING & CHECKING ----------

# Membership
"Hello" in text                         # True

# startswith() / endswith()
text.startswith("  He")                 # True
text.endswith("!  ")                    # True

# find() - returns lowest index of substring (-1 if not found)
idx = text.find("World")                # 7

# rfind() - returns highest index
ridx = text.rfind("l")                  # 10

# index() - like find but raises ValueError if not found
try:
    pos = text.index("World")           # 7
except ValueError:
    pass

# count() - number of non-overlapping occurrences
cnt = text.count("l")                   # 3

# isalnum() / isalpha() / isdigit() / isspace()
text.isalnum()                          # False (space, !)
text.isalpha()                          # False
text.isdigit()                          # False
"   ".isspace()                         # True

# isupper() / islower()
"HELLO".isupper()                       # True
"hello".islower()                       # True


# ---------- 4. SLICING & INDEXING ----------

text = "Python"

# Indexing (0-based, negative from end)
text[0]      # 'P'
text[-1]     # 'n'

# Slicing [start:stop:step] (stop exclusive)
text[1:4]    # 'yth' (indices 1,2,3)
text[:3]     # 'Pyt'
text[3:]     # 'hon'
text[::2]    # 'Pto'
text[::-1]   # 'nohtyP'

# Length
len(text)    # 6


# ---------- 5. FORMATTING ----------

name = "Alice"
age = 30
pi = 3.14159

# f-string (Python 3.6+)
print(f"{name} is {age} years old")
print(f"Pi = {pi:.2f}")                 # "Pi = 3.14"
print(f"Number: {42:05d}")              # "Number: 00042"

# .format() method
print("{} is {} years old".format(name, age))
print("{1} is {0} years old".format(age, name))  # positional
print("{name} is {age} years old".format(name="Alice", age=30))

# %-formatting (old style)
print("%s is %d years old" % (name, age))

# Multiple arguments to print
print(name, "is", age, "years old")


# ---------- 6. ADDITIONAL USEFUL METHODS ----------

# center() - centers string in a given width
"Hello".center(11)                      # "   Hello   "

# ljust() / rjust() - left or right justify
"Hello".ljust(10)                       # "Hello     "
"Hello".rjust(10)                       # "     Hello"

# zfill() - pads with zeros on the left
"42".zfill(5)                           # "00042"

# partition() - splits into (head, separator, tail)
head, sep, tail = "name:value".partition(":")  # head="name", sep=":", tail="value"

# encode() / decode() - convert to bytes and back
b = "Hello".encode("utf-8")             # b'Hello'
s = b.decode("utf-8")                   # "Hello"