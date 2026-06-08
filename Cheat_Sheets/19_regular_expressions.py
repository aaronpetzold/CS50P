# === Regular Expressions (regex) ===


# ========== TABLE OF CONTENTS ==========
#
# 1. IMPORT
# 2. BASIC FUNCTIONS
# 3. SPECIAL CHARACTERS
# 4. CHARACTER CLASSES (shorthand)
# 5. QUANTIFIERS EXAMPLE
# 6. ANCHORS
# 7. GROUPS AND CAPTURING
# 8. FLAGS (MODIFIERS)
# 9. ESCAPING SPECIAL CHARACTERS
# 10. COMMON PATTERNS
# 11. PRACTICAL EXAMPLES
# 12. QUICK REFERENCE
#
# ========================================


# Definition: Regular expressions are patterns used to match, search, and manipulate text
# based on specific rules.


# ---------- 1. IMPORT ----------
# Definition: The re module provides regex functionality in Python.

import re



# ---------- 2. BASIC FUNCTIONS ----------

# re.search(pattern, string)
# Definition: Finds first occurrence anywhere in the string. Returns a match object or None.

match = re.search(r"hello", "Say hello there")
if match:
    print("Found")                    # "Found"


# re.match(pattern, string)
# Definition: Matches only at the beginning of the string.

match = re.match(r"hello", "hello world")   # ✅ matches
match = re.match(r"hello", "say hello")     # ❌ None (not at start)


# re.findall(pattern, string)
# Definition: Returns a list of all non-overlapping matches.

words = re.findall(r"\w+", "Hello world! Python is great.")
print(words)   # ['Hello', 'world', 'Python', 'is', 'great']


# re.finditer(pattern, string)
# Definition: Returns an iterator of match objects (useful for getting positions).

for match in re.finditer(r"\d+", "I have 2 apples and 3 oranges"):
    print(match.group(), match.start())   # "2 7", "3 19"


# re.sub(pattern, repl, string)
# Definition: Replaces all matches with a replacement string.

text = "My phone is 123-456-7890."
cleaned = re.sub(r"\D", "", text)   # remove non-digits
print(cleaned)   # "1234567890"


# re.split(pattern, string)
# Definition: Splits the string at each match.

parts = re.split(r"[ ,]+", "Hello world, Python")
print(parts)   # ['Hello', 'world', 'Python']


# re.compile(pattern)
# Definition: Precompiles a regex for efficiency (use when pattern is reused many times).

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
result = pattern.search("Call 123-456-7890 now")
print(result.group())   # "123-456-7890"



# ---------- 3. SPECIAL CHARACTERS ----------
#
# .        - any character except newline
# ^        - start of string
# $        - end of string
# *        - 0 or more repetitions of the preceding character/group
# +        - 1 or more repetitions
# ?        - 0 or 1 repetition
# {m}      - exactly m repetitions
# {m,n}    - between m and n repetitions
# []       - set of characters (e.g., [a-z] any lowercase letter)
# [^...] – negated character class (matches anything not in the set)
# |        - OR (e.g., cat|dog)
# ()       - capturing group
# (?:...)  - non-capturing version
# \        - escape special character



# ---------- 4. CHARACTER CLASSES (SHORTHAND) ----------
#
# \d       - any digit (0-9)           equivalent to [0-9]
# \D       - any non-digit
# \w       - any letter, digit, or underscore  [a-zA-Z0-9_]
# \W       - any non-word character
# \s       - any whitespace (space, tab, newline)
# \S       - any non-whitespace
# \b       - word boundary (e.g., r"\bcat\b" matches whole word "cat")
# \B       - non-word boundary



# ---------- 5. QUANTIFIERS EXAMPLE ----------

text = "aa aaa aaaa"

re.findall(r"a{2}", text)       # ['aa', 'aa', 'aa'] (non-overlapping)
re.findall(r"a{2,}", text)      # ['aa', 'aaa', 'aaaa'] (2 or more)
re.findall(r"a{2,3}", text)     # ['aa', 'aaa', 'aaa'] (2-3)



# ---------- 6. ANCHORS ----------
#
# ^ - start of string (or line with MULTILINE flag)
# $ - end of string (or line with MULTILINE flag)

re.search(r"^Hello", "Hello world")     # matches
re.search(r"world$", "Hello world")     # matches



# ---------- 7. GROUPS AND CAPTURING ----------

# Parentheses create capturing groups.

match = re.search(r"(\d{3})-(\d{3})-(\d{4})", "123-456-7890")
if match:
    print(match.group(0))     # "123-456-7890" (full match)
    print(match.group(1))     # "123"
    print(match.group(2))     # "456"
    print(match.group(3))     # "7890"
    print(match.groups())     # ('123', '456', '7890')


# Non-capturing group (?:...) - doesn't create a backreference.

match = re.search(r"(?:\d{3}-){2}\d{4}", "123-456-7890")   # matches but no groups


# Named groups (?P<name>...)

match = re.search(r"(?P<area>\d{3})-(?P<exchange>\d{3})-(?P<number>\d{4})", "123-456-7890")
print(match.group("area"))    # "123"



# ---------- 8. FLAGS (MODIFIERS) ----------
#
# re.IGNORECASE (re.I)   - case-insensitive matching
# re.MULTILINE (re.M)    - ^ and $ match start/end of each line, not just whole string
# re.DOTALL (re.S)       - . matches newline as well
# re.VERBOSE (re.X)      - allow whitespace and comments in pattern

# Example: case-insensitive
re.search(r"hello", "HELLO", re.IGNORECASE)   # matches


# Example: multiline
text = "line1\nline2\nline3"
re.findall(r"^line", text, re.MULTILINE)   # ['line', 'line', 'line']


# Example: verbose (pattern can be split over lines with comments)
pattern = re.compile(r"""
    \d{3}    # area code
    -        # dash
    \d{3}    # exchange
    -        # dash
    \d{4}    # number
""", re.VERBOSE)



# ---------- 9. ESCAPING SPECIAL CHARACTERS ----------

# Use re.escape() to auto-escape all special characters.

literal = re.escape("2 + 2 = 4")   # "2\ \+\ 2\ =\ 4"
print(re.search(literal, "2 + 2 = 4"))   # matches

# Or manually prepend backslash: \., \*, \+, \?, \[, \], \(, \), \{, \}, \|, \^, \$

# re.escape() is useful when building regex from user input.



# ---------- 10. COMMON PATTERNS ----------

# Email (simplified)
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Phone number (US format)
phone_pattern = r"\d{3}[-.]?\d{3}[-.]?\d{4}"

# URL
url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

# IPv4 address
ipv4_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# Date YYYY-MM-DD
date_pattern = r"\d{4}-\d{2}-\d{2}"



# ---------- 11. PRACTICAL EXAMPLES ----------

# Validate a username (alphanumeric + underscore, 3-16 chars)
username = "john_doe"
if re.match(r"^[a-zA-Z0-9_]{3,16}$", username):
    print("Valid username")


# Extract all hashtags from text
hashtags = re.findall(r"#\w+", "Python is #awesome and #fun")
print(hashtags)   # ['#awesome', '#fun']


# Replace multiple spaces with single space
text = "This   has   many    spaces"
clean = re.sub(r"\s+", " ", text)
print(clean)   # "This has many spaces"


# Split by commas or spaces
parts = re.split(r"[ ,]+", "apple, banana  orange,grape")
print(parts)   # ['apple', 'banana', 'orange', 'grape']


# Remove HTML tags (very basic)
html = "<p>Hello <b>world</b></p>"
text = re.sub(r"<[^>]+>", "", html)
print(text)   # "Hello world"



# ---------- 12. QUICK REFERENCE ----------
#
# | Function          | Purpose                                 |
# |-------------------|-----------------------------------------|
# | re.search()       | Find first match anywhere               |
# | re.match()        | Find match at start of string           |
# | re.findall()      | Return list of all matches              |
# | re.finditer()     | Return iterator of match objects        |
# | re.sub()          | Replace matches                         |
# | re.split()        | Split string at matches                 |
# | re.compile()      | Precompile pattern for reuse            |
# | re.escape()       | Escape all regex special characters     |
#
# | Common pattern    | Meaning                                 |
# |-------------------|-----------------------------------------|
# | .                 | Any character (except newline)          |
# | \d                | Digit [0-9]                             |
# | \w                | Word [a-zA-Z0-9_]                       |
# | \s                | Whitespace                              |
# | ^                 | Start of string                         |
# | $                 | End of string                           |
# | *                 | 0 or more                               |
# | +                 | 1 or more                               |
# | ?                 | 0 or 1                                  |
# | {n}               | Exactly n                               |
# | {n,m}             | Between n and m                         |
# | [abc]             | a, b, or c                              |
# | [^abc]            | Not a, b, or c                          |
# | a|b               | a or b                                  |
# | (...)             | Capturing group                         |
# | (?:...)           | Non-capturing group                     |
# | (?P<name>...)     | Named group                             |