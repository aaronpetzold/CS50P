# === Regular Expressions (regex) ===


# ========== TABLE OF CONTENTS ==========
#
# 1. IMPORT
# 2. BASIC FUNCTIONS (search, match, findall, finditer, sub, subn, split, compile, fullmatch)
# 3. SPECIAL CHARACTERS
# 4. CHARACTER CLASSES (shorthand)
# 5. QUANTIFIERS (greedy vs lazy)
# 6. ANCHORS
# 7. GROUPS AND CAPTURING
# 8. LOOKAHEAD AND LOOKBEHIND (positive/negative)
# 9. BACKREFERENCES
# 10. FLAGS (MODIFIERS)
# 11. ESCAPING SPECIAL CHARACTERS
# 12. COMMON PATTERNS (enhanced)
# 13. PRACTICAL EXAMPLES (more realistic)
# 14. QUICK REFERENCE
#
# ========================================


# Definition: Regular expressions are patterns used to match, search, and manipulate text
# based on specific rules.


# ---------- 1. IMPORT ----------

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
match = re.match(r"hello", "say hello")     # ❌ None

# re.fullmatch(pattern, string)
# Definition: Requires the entire string to match the pattern (Python 3.4+).

match = re.fullmatch(r"\d+", "123")         # ✅ matches
match = re.fullmatch(r"\d+", "123abc")      # ❌ None

# re.findall(pattern, string)
# Definition: Returns a list of all non-overlapping matches.

words = re.findall(r"\w+", "Hello world! Python is great.")
print(words)   # ['Hello', 'world', 'Python', 'is', 'great']

# re.finditer(pattern, string)
# Definition: Returns an iterator of match objects (useful for positions).

for match in re.finditer(r"\d+", "I have 2 apples and 3 oranges"):
    print(match.group(), match.start())   # "2 7", "3 19"

# re.sub(pattern, repl, string, count=0)
# Definition: Replaces all matches with a replacement string (or callable).

text = "My phone is 123-456-7890."
cleaned = re.sub(r"\D", "", text)   # remove non-digits
print(cleaned)   # "1234567890"

# re.subn() – same as sub but also returns count of replacements.
result, count = re.subn(r"\d", "X", "a1b2c3")
print(result, count)   # "aXbXcX 3"

# re.split(pattern, string, maxsplit=0)
# Definition: Splits the string at each match.

parts = re.split(r"[ ,]+", "Hello world, Python")
print(parts)   # ['Hello', 'world', 'Python']

# re.compile(pattern, flags=0)
# Definition: Precompiles a regex for efficiency (reuse many times).

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
result = pattern.search("Call 123-456-7890 now")
print(result.group())   # "123-456-7890"


# ---------- 3. SPECIAL CHARACTERS ----------
#
# .        - any character except newline (use re.DOTALL to include newline)
# ^        - start of string (or line with MULTILINE)
# $        - end of string (or line with MULTILINE)
# *        - 0 or more repetitions of the preceding character/group
# +        - 1 or more repetitions
# ?        - 0 or 1 repetition
# {m}      - exactly m repetitions
# {m,n}    - between m and n repetitions (n can be omitted)
# []       - set of characters (e.g., [a-z] any lowercase letter)
# [^...]   - negated character class (matches anything not in the set)
# |        - OR (e.g., cat|dog)
# ()       - capturing group
# (?:...)  - non-capturing group
# \        - escape special character


# ---------- 4. CHARACTER CLASSES (SHORTHAND) ----------
#
# \d       - any digit (0-9)           equivalent to [0-9]
# \D       - any non-digit
# \w       - any letter, digit, or underscore  [a-zA-Z0-9_]
# \W       - any non-word character
# \s       - any whitespace (space, tab, newline)
# \S       - any non-whitespace
# \b       - word boundary (matches between word [\w] and non-word [\W] or edge)
# \B       - non-word boundary


# ---------- 5. QUANTIFIERS (greedy vs lazy) ----------

text = "aa aaa aaaa"

# Greedy (default): matches as much as possible
re.findall(r"a+", text)       # ['aa', 'aaa', 'aaaa']
re.findall(r"a{2,}", text)    # ['aa', 'aaa', 'aaaa']

# Lazy (add `?`): matches as little as possible
re.findall(r"a+?", text)      # ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'] (each single a)
re.findall(r"a{2,}?", text)   # ['aa', 'aa', 'aa'] (two a's at a time)

# Example: extracting HTML tags
html = "<div><span>text</span></div>"
greedy = re.search(r"<.*>", html).group()      # "<div><span>text</span></div>" (entire)
lazy = re.search(r"<.*?>", html).group()       # "<div>" (smallest)


# ---------- 6. ANCHORS ----------
#
# ^ - start of string (or line with MULTILINE)
# $ - end of string (or line with MULTILINE)
# \A - start of string (ignores MULTILINE)
# \Z - end of string (ignores MULTILINE)
# \b - word boundary
# \B - non-word boundary

re.search(r"^Hello", "Hello world")     # matches
re.search(r"world$", "Hello world")     # matches
re.search(r"\AHello", "Hello world")    # matches, ignores multiline
re.search(r"world\Z", "Hello world")    # matches

# Word boundary: match whole word "cat" only
re.findall(r"\bcat\b", "cat catalina scat")   # ['cat']


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

# Using groups in replacement (with re.sub)
re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"(\1) \2-\3", "123-456-7890")  # "(123) 456-7890"


# ---------- 8. LOOKAHEAD AND LOOKBEHIND (zero‑width assertions) ----------
#
# Positive lookahead: (?=...)   – matches if pattern follows, but does not consume.
# Negative lookahead: (?!...)   – matches if pattern does NOT follow.
# Positive lookbehind: (?<=...) – matches if pattern precedes, but does not consume.
# Negative lookbehind: (?<!...) – matches if pattern does NOT precede.

# Example: match "foo" only if followed by "bar"
match = re.search(r"foo(?=bar)", "foobar")
print(match.group())          # "foo" (bar is not included)

# Example: match "foo" only if NOT followed by "bar"
match = re.search(r"foo(?!bar)", "foobaz")
print(match.group())          # "foo"

# Example: match "bar" only if preceded by "foo"
match = re.search(r"(?<=foo)bar", "foobar")
print(match.group())          # "bar"

# Example: match "bar" only if NOT preceded by "foo"
match = re.search(r"(?<!foo)bar", "bazbar")
print(match.group())          # "bar"

# Practical: find all numbers not followed by a percent sign
re.findall(r"\d+(?!%)", "10% 20 30% 40")   # ['20', '40']


# ---------- 9. BACKREFERENCES ----------
#
# Backreference to a capturing group: \1, \2, etc.

# Match doubled words (e.g., "the the")
match = re.search(r"\b(\w+)\s+\1\b", "the the")
print(match.group())          # "the the"

# Match repeated digits (e.g., "11", "22")
re.findall(r"(\d)\1", "112233")   # ['1', '2', '3']

# Use inside replacement: re.sub(r"(\w+) \1", r"\1", "the the")

# Backreference to named group: (?P=name)
re.search(r"(?P<word>\b\w+\b)\s+(?P=word)", "hello hello")  # matches


# ---------- 10. FLAGS (MODIFIERS) ----------
#
# re.IGNORECASE (re.I)   - case-insensitive matching
# re.MULTILINE (re.M)    - ^ and $ match start/end of each line (not just whole string)
# re.DOTALL (re.S)       - . matches newline as well
# re.VERBOSE (re.X)      - allow whitespace and comments in pattern
# re.ASCII (re.A)        - make \w, \b, \d, \s match only ASCII characters
# re.LOCALE (re.L)       - use locale-dependent matching (rarely used)

# Example: case-insensitive
re.search(r"hello", "HELLO", re.IGNORECASE)   # matches

# Example: multiline (^ and $ per line)
text = "line1\nline2\nline3"
re.findall(r"^line", text, re.MULTILINE)   # ['line', 'line', 'line']

# Example: DOTALL (dot matches newline)
text = "hello\nworld"
re.search(r"hello.world", text, re.DOTALL)   # matches (dot includes newline)

# Example: VERBOSE (pattern with comments and whitespace)
pattern = re.compile(r"""
    \d{3}    # area code
    -        # dash
    \d{3}    # exchange
    -        # dash
    \d{4}    # number
""", re.VERBOSE)

# Combine flags with | (bitwise OR)
re.search(r"^hello", text, re.IGNORECASE | re.MULTILINE)


# ---------- 11. ESCAPING SPECIAL CHARACTERS ----------

# re.escape() auto-escapes all regex special characters.

literal = re.escape("2 + 2 = 4")   # "2\ \+\ 2\ =\ 4"
print(re.search(literal, "2 + 2 = 4"))   # matches

# Manual escaping: prepend backslash to . * + ? [ ] ( ) { } | \ ^ $


# ---------- 12. COMMON PATTERNS (enhanced) ----------

# Email (RFC 5322 simplified, but practical)
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Phone number (US, flexible)
phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"

# URL (http/https)
url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

# IPv4 address (with strict range validation via regex)
ipv4_pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"

# Date YYYY-MM-DD (simple, not validating month/day ranges)
date_pattern = r"\d{4}-\d{2}-\d{2}"

# Hexadecimal color (e.g., #a3f5c2 or #ABC)
hex_color = r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b"

# US ZIP code (5 digits, optional +4)
zip_pattern = r"\b\d{5}(?:-\d{4})?\b"

# Time HH:MM (24-hour)
time_pattern = r"\b(?:[01]\d|2[0-3]):[0-5]\d\b"


# ---------- 13. PRACTICAL EXAMPLES (more realistic) ----------

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

# Remove HTML tags (basic)
html = "<p>Hello <b>world</b></p>"
text = re.sub(r"<[^>]+>", "", html)
print(text)   # "Hello world"

# Find all email addresses in a text
text = "Contact: alice@example.com, bob@test.co.uk"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)   # ['alice@example.com', 'bob@test.co.uk']

# Extract domain from email
match = re.search(r"@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", "alice@example.com")
if match:
    print(match.group(1))   # "example.com"

# Parse log lines (e.g., "ERROR 2024-01-15: Disk full")
log = "ERROR 2024-01-15: Disk full"
match = re.search(r"(\w+) (\d{4}-\d{2}-\d{2}): (.*)", log)
if match:
    level, date, msg = match.groups()
    print(level, date, msg)


# ---------- 14. QUICK REFERENCE ----------
#
# | Function            | Purpose                                         |
# |---------------------|-------------------------------------------------|
# | re.search()         | Find first match anywhere                      |
# | re.match()          | Find match at start of string                  |
# | re.fullmatch()      | Require entire string to match                 |
# | re.findall()        | Return list of all matches                     |
# | re.finditer()       | Return iterator of match objects               |
# | re.sub()            | Replace matches (string or callable)           |
# | re.subn()           | Same as sub, plus count of replacements        |
# | re.split()          | Split string at matches                        |
# | re.compile()        | Precompile pattern for reuse                   |
# | re.escape()         | Escape all regex special characters            |
#
# | Common pattern      | Meaning                                         |
# |---------------------|-------------------------------------------------|
# | .                   | Any character (except newline)                  |
# | \d                  | Digit [0-9]                                     |
# | \w                  | Word [a-zA-Z0-9_]                               |
# | \s                  | Whitespace                                      |
# | \b                  | Word boundary                                   |
# | ^                   | Start of string (or line)                       |
# | $                   | End of string (or line)                         |
# | *                   | 0 or more (greedy)                              |
# | *?                  | 0 or more (lazy)                                |
# | +                   | 1 or more (greedy)                              |
# | +?                  | 1 or more (lazy)                                |
# | ?                   | 0 or 1                                          |
# | {n}                 | Exactly n                                       |
# | {n,m}               | Between n and m (greedy)                        |
# | {n,m}?              | Between n and m (lazy)                          |
# | [abc]               | a, b, or c                                      |
# | [^abc]              | Not a, b, or c                                  |
# | a|b                 | a or b                                          |
# | (...)               | Capturing group                                 |
# | (?:...)             | Non-capturing group                             |
# | (?P<name>...)       | Named group                                     |
# | (?=...)             | Positive lookahead                              |
# | (?!...)             | Negative lookahead                              |
# | (?<=...)            | Positive lookbehind                             |
# | (?<!...)            | Negative lookbehind                             |
# | \1, \2              | Backreference to capturing group                |
# | (?P=name)           | Backreference to named group                    |