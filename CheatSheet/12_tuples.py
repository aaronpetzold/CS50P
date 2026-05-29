# === Tuples ===

# === CREATION & BASICS ===

# 5 Ways to create tuples
tuple1 = ()                                 # Empty tuple
tuple2 = (1, 2, 3)                         # Normal
tuple3 = 1, 2, 3                           # Parentheses optional
tuple4 = tuple([1, 2, 3])                  # From list
tuple5 = tuple("hello")                    # From string → ('h','e','l','l','o')

# Single element NEEDS comma!
single = (42,)                             # Tuple with one element
not_tuple = (42)                           # ❌ Just integer 42!

# Mixed types
mixed = ("text", 42, 3.14, True, None, [1, 2], {"key": "value"})

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))

# === ACCESSING ELEMENTS ===

t = (10, 20, 30, 40, 50, 60, 70)

# Positive indexing (0-based)
t[0]                                       # 10 (first)
t[3]                                       # 40 (fourth)

# Negative indexing (from end)
t[-1]                                      # 70 (last)
t[-2]                                      # 60 (second last)

# Slicing [start:stop:step] (stop EXCLUSIVE!)
t[1:4]                                     # (20, 30, 40)
t[:3]                                      # (10, 20, 30) (first 3)
t[3:]                                      # (40, 50, 60, 70) (from 3rd)
t[::2]                                     # (10, 30, 50, 70) (every 2nd)
t[::-1]                                    # (70, 60, 50, 40, 30, 20, 10) (reverse!)

# Get portions
first_two = t[:2]                          # (10, 20)
last_two = t[-2:]                          # (60, 70)
all_but_ends = t[1:-1]                     # (20, 30, 40, 50, 60)

# === UNPACKING (SUPER USEFUL!) ===

# Basic unpacking
x, y, z = (1, 2, 3)                        # x=1, y=2, z=3

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)     # first=1, middle=[2,3,4], last=5
*start, last_two, last_one = (1, 2, 3, 4, 5)  # start=[1,2,3], last_two=4, last_one=5

# Ignore elements with _
a, _, b = (1, 2, 3)                        # a=1, b=3 (ignore 2)
a, *_, b = (1, 2, 3, 4, 5)                 # a=1, b=5 (ignore middle)

# Swap variables
x, y = 10, 20
x, y = y, x                                # x=20, y=10

# === TUPLE OPERATIONS ===

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
combined = t1 + t2                         # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3                          # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Comparison (lexicographical)
(1, 2, 3) < (1, 2, 4)                      # True
("a", "b") > ("a", "a")                    # True

# Membership
3 in t1                                    # True
7 not in t1                                # True

# Length and checking
len(t1)                                    # 3
bool(t1)                                   # True (non-empty)
bool(())                                   # False (empty)

# === TUPLE METHODS ===

t = (1, 2, 2, 3, 4, 2, 5)

t.count(2)                                 # 3 (count occurrences)
t.index(3)                                 # 3 (find first position)

# min, max, sum
min(t)                                     # 1
max(t)                                     # 5
sum(t)                                     # 19

# === IMMUTABILITY NOTES ===

# Tuples are IMMUTABLE
t = (1, 2, 3)
# t[0] = 10                                # ❌ TypeError!

# But can contain mutable objects
t = ([1, 2], [3, 4])
t[0].append(3)                             # ✅ OK! List inside can change
# t now: ([1, 2, 3], [3, 4])

# === PRACTICAL PATTERNS ===

# Return multiple values from function
def get_user_info():
    return "John", 30, "john@example.com"

name, age, email = get_user_info()

# Dictionary keys (must be immutable)
locations = {
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris"
}

# Namedtuples (like lightweight classes)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)                            # 10 20

# Record-like data
people = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Designer"),
    ("Charlie", 35, "Manager")
]

for name, age, job in people:
    print(f"{name} ({age}) works as {job}")