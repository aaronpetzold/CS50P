# === Sets ===


# ========== TABLE OF CONTENTS ==========
#
# 1. CREATION (4 ways)
# 2. ADDING & REMOVING ELEMENTS
# 3. SET OPERATIONS (union, intersection, difference, symmetric difference)
# 4. COMPARISONS & CHECKS (subset, superset, disjoint, membership)
# 5. SET COMPREHENSION
# 6. PRACTICAL PATTERNS (deduplication, common elements, missing keys)
# 7. FROZENSET (immutable version)
#
# ========================================


# Definition: Sets are unordered collections of unique, immutable objects.
# They support fast membership tests and mathematical set operations.


# ---------- 1. CREATION (4 ways) ----------

set1 = set()                                # Empty (NOT {} - that's a dict)
set2 = {"apple", "banana", "cherry"}        # Literal
set3 = set(["apple", "banana", "cherry"])   # From list (removes duplicates)
set4 = set("hello")                         # From string → {'h','e','l','o'}

# Mixed types allowed (but elements must be hashable – no lists or dicts inside)
mixed_set = {1, "hello", 3.14, True, (1, 2)}  # tuple is OK


# ---------- 2. ADDING & REMOVING ELEMENTS ----------

fruits = {"apple", "banana"}

# Adding
fruits.add("cherry")                        # {'apple','banana','cherry'}
fruits.update(["orange", "grape"])          # add multiple → {'apple','banana','cherry','orange','grape'}
fruits |= {"mango", "kiwi"}                 # same as update

# Removing
fruits.remove("banana")                     # removes "banana", raises KeyError if missing
fruits.discard("watermelon")                # removes if present, does nothing otherwise
popped = fruits.pop()                       # removes and returns an arbitrary element
fruits.clear()                              # empty set


# ---------- 3. SET OPERATIONS (union, intersection, difference, symmetric difference) ----------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (OR): elements in A or B
union = A | B                               # {1,2,3,4,5,6}
union = A.union(B)                          # same

# Intersection (AND): elements in both A and B
intersection = A & B                        # {3,4}
intersection = A.intersection(B)            # same

# Difference (A - B): elements in A but not in B
difference = A - B                          # {1,2}
difference = A.difference(B)                # same

# Symmetric difference (XOR): elements in A or B but not both
sym_diff = A ^ B                            # {1,2,5,6}
sym_diff = A.symmetric_difference(B)        # same

# Update versions (modify the original set in place)
A.update(B)                                 # A becomes A | B
A.intersection_update(B)                    # A becomes A & B
A.difference_update(B)                      # A becomes A - B
A.symmetric_difference_update(B)            # A becomes A ^ B


# ---------- 4. COMPARISONS & CHECKS (subset, superset, disjoint, membership) ----------

X = {1, 2}
Y = {1, 2, 3}
Z = {4, 5}

X.issubset(Y)                               # True (all X in Y)
Y.issuperset(X)                             # True (Y contains all X)
X.isdisjoint(Z)                             # True (no common elements)

# Membership (O(1) average)
2 in A                                      # True
7 not in A                                  # True

# Size and copy
len(A)                                      # number of elements
copy_of_A = A.copy()                        # shallow copy


# ---------- 5. SET COMPREHENSION ----------

# Basic: {expression for item in iterable}
squares = {x**2 for x in range(5)}          # {0,1,4,9,16}

# With condition
evens = {x for x in range(10) if x % 2 == 0}  # {0,2,4,6,8}

# From list with transformation
words = ["hello", "world", "python"]
lengths = {len(word) for word in words}     # {5,6} (unique lengths)


# ---------- 6. PRACTICAL PATTERNS (deduplication, common elements, missing keys) ----------

# Remove duplicates from a list (order may change)
numbers = [1, 2, 2, 3, 3, 4, 4, 4]
unique = list(set(numbers))                 # [1,2,3,4]

# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)            # {4,5}

# Check which required keys are missing from a dictionary
required = {"ID", "name", "email"}
user_data = {"name": "John", "email": "john@example.com"}
missing = required - set(user_data.keys())  # {"ID"}

# Count unique words in a string
text = "hello world hello python"
unique_words = len(set(text.split()))       # 3


# ---------- 7. FROZENSET (immutable version) ----------

# frozenset is an immutable set; can be used as a dictionary key.
frozen = frozenset([1, 2, 3])               # frozenset({1,2,3})
# frozen.add(4)                             # AttributeError (immutable)

# Supports the same set operations but returns new frozensets.
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])
fs_union = fs1 | fs2                        # frozenset({1,2,3,4,5})