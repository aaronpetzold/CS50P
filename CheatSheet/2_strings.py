# === Strings ===

text = "  Hello World!  "

# Methods
clean = text.strip()                # "Hello World!"
lower = text.lower()                # "  hello world!  "
upper = text.upper()                # "  HELLO WORLD!  "
replaced = text.replace("World", "Python")  # "  Hello Python!  "
words = text.split()                # ["Hello", "World!"]
joined = "-".join(["a", "b", "c"])  # "a-b-c"

# Checks
"Hello" in text                     # True
text.startswith("  He")             # True
text.endswith("!  ")                # True
text.isalnum()                      # numbers and letters
text.isalpha()                      # checks if all characters are letters
text.isdigit()                      # checks if all characters are digits

# Slicing (same as lists)
text[3:8]                           # "Hello"
text[:5]                            # "  Hel"
text[-6:]                           # "World!"

# String indexing 
text = "Python"
text[0]     # 'P' (first character)
text[-1]    # 'n' (last character)
text[1:4]   # 'yth' (slice)
len(text)   # 6 (length)

# Formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")       # f-string
print("{} is {} years old".format(name, age))  # .format()
print(name, "is", age, "years old")       # Multiple args
