# === Tuples ===


# ========== TABLE OF CONTENTS ==========
#
# 1. CREATION (5 ways)
# 2. ACCESSING ELEMENTS (indexing, slicing)
# 3. UNPACKING (basic, extended, ignoring elements)
# 4. TUPLE OPERATIONS (concatenation, repetition, comparison, membership)
# 5. TUPLE METHODS (count, index)
# 6. IMMUTABILITY NOTES (including mutable inside)
# 7. PRACTICAL PATTERNS (multiple returns, dict keys, namedtuple, record‑like data)
#
# ========================================


# Definition: Tuples are immutable, ordered sequences that can contain any type of element.
# They are often used for fixed collections or to return multiple values from a function.


# ---------- 1. CREATION (5 ways) ----------

tuple1 = ()                                 # Empty tuple
tuple2 = (1, 2, 3)                          # Normal
tuple3 = 1, 2, 3                            # Parentheses optional
tuple4 = tuple([1, 2, 3])                   # From list
tuple5 = tuple("hello")                     # From string → ('h','e','l','l','o')

# Single element NEEDS a trailing comma!
single = (42,)                              # Correct tuple with one element
not_tuple = (42)                            # ❌ Just integer 42!

# Mixed types are allowed
mixed = ("text", 42, 3.14, True, None, [1, 2], {"key": "value"})

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))


# ---------- 2. ACCESSING ELEMENTS (indexing, slicing) ----------

t = (10, 20, 30, 40, 50, 60, 70)

# Positive indexing (0‑based)
t[0]                                       # 10 (first)
t[3]                                       # 40 (fourth)

# Negative indexing (from the end)
t[-1]                                      # 70 (last)
t[-2]                                      # 60 (second last)

# Slicing [start:stop:step] (stop is exclusive)
t[1:4]                                     # (20, 30, 40)
t[:3]                                      # (10, 20, 30)  (first 3)
t[3:]                                      # (40, 50, 60, 70) (from index 3)
t[::2]                                     # (10, 30, 50, 70) (every 2nd)
t[::-1]                                    # (70,60,50,40,30,20,10) (reverse)

# Get portions
first_two = t[:2]                          # (10, 20)
last_two = t[-2:]                          # (60, 70)
all_but_ends = t[1:-1]                     # (20, 30, 40, 50, 60)


# ---------- 3. UNPACKING (basic, extended, ignoring elements) ----------

# Basic unpacking – number of variables must match tuple length.
x, y, z = (1, 2, 3)                        # x=1, y=2, z=3

# Extended unpacking using * (rest becomes a list)
first, *middle, last = (1, 2, 3, 4, 5)     # first=1, middle=[2,3,4], last=5
*start, last_two, last_one = (1, 2, 3, 4, 5)  # start=[1,2,3], last_two=4, last_one=5

# Ignore elements with underscore
a, _, b = (1, 2, 3)                        # a=1, b=3 (2 is ignored)
a, *_, b = (1, 2, 3, 4, 5)                 # a=1, b=5 (middle ignored)

# Swap variables using tuple unpacking
x, y = 10, 20
x, y = y, x                                # x=20, y=10


# ---------- 4. TUPLE OPERATIONS (concatenation, repetition, comparison, membership) ----------

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation – creates a new tuple.
combined = t1 + t2                         # (1,2,3,4,5,6)

# Repetition
repeated = t1 * 3                          # (1,2,3,1,2,3,1,2,3)

# Lexicographical comparison
(1, 2, 3) < (1, 2, 4)                      # True
("a", "b") > ("a", "a")                    # True

# Membership checks
3 in t1                                    # True
7 not in t1                                # True

# Length and boolean evaluation
len(t1)                                    # 3
bool(t1)                                   # True (non‑empty)
bool(())                                   # False (empty)


# ---------- 5. TUPLE METHODS (count, index) ----------

t = (1, 2, 2, 3, 4, 2, 5)

t.count(2)                                 # 3 (how many times 2 appears)
t.index(3)                                 # 3 (first position of 3)

# Built‑in functions also work:
min(t)                                     # 1
max(t)                                     # 5
sum(t)                                     # 19


# ---------- 6. IMMUTABILITY NOTES (including mutable inside) ----------

# Tuples themselves are immutable – you cannot change, add, or remove elements.
t = (1, 2, 3)
# t[0] = 10                                # ❌ TypeError: 'tuple' object does not support item assignment

# However, if a tuple contains a mutable object (like a list), that object can be modified.
t = ([1, 2], [3, 4])
t[0].append(3)                             # ✅ OK! The list inside changes
# t now: ([1, 2, 3], [3, 4])               # The tuple still holds the same list objects.


# ---------- 7. PRACTICAL PATTERNS (multiple returns, dict keys, namedtuple, record‑like data) ----------

# 1. Returning multiple values from a function.
def get_user_info():
    return "John", 30, "john@example.com"

name, age, email = get_user_info()

# 2. Using tuples as dictionary keys (they are hashable).
locations = {
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris"
}

# 3. Lightweight classes with namedtuple.
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)                            # 10 20

# 4. Representing records (e.g., rows from a database).
people = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Designer"),
    ("Charlie", 35, "Manager")
]
for name, age, job in people:
    print(f"{name} ({age}) works as {job}")