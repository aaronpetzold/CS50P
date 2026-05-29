# === Sets ===

# === CREATION & BASICS ===

# 4 Ways to create sets
set1 = set()                                # Empty (NOT {} - that's dict!)
set2 = {"apple", "banana", "cherry"}        # Literal
set3 = set(["apple", "banana", "cherry"])   # From list (removes duplicates)
set4 = set("hello")                         # From string → {'h','e','l','o'}

# Mixed types allowed
mixed_set = {1, "hello", 3.14, True, (1, 2)}  # Can't have lists/dicts inside!

# Frozen sets (immutable)
frozen = frozenset([1, 2, 3])               # Cannot modify
# frozen.add(4)                             # ❌ AttributeError!

# === ADDING & REMOVING ===

fruits = {"apple", "banana"}

# Add elements
fruits.add("cherry")                        # {'apple', 'banana', 'cherry'}
fruits.update(["orange", "grape"])          # Add multiple → {'apple','banana','cherry','orange','grape'}
fruits |= {"mango", "kiwi"}                 # Union update (same as update)

# Remove elements
fruits.remove("banana")                     # Remove specific (ERROR if missing)
fruits.discard("watermelon")                # Remove (NO ERROR if missing)
popped = fruits.pop()                       # Remove random element, return it
fruits.clear()                              # Empty set → set()

# === SET OPERATIONS ===

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (OR): elements in A OR B
union = A | B                               # {1, 2, 3, 4, 5, 6}
union = A.union(B)                          # Same

# Intersection (AND): elements in A AND B
intersection = A & B                        # {3, 4}
intersection = A.intersection(B)            # Same

# Difference (A - B): elements in A NOT in B
difference = A - B                          # {1, 2}
difference = A.difference(B)                # Same

# Symmetric Difference (XOR): elements in A OR B but NOT both
sym_diff = A ^ B                            # {1, 2, 5, 6}
sym_diff = A.symmetric_difference(B)        # Same

# Update versions (modify original)
A.update(B)                                 # A = A | B
A.intersection_update(B)                    # A = A & B
A.difference_update(B)                      # A = A - B

# === COMPARISONS & CHECKS ===

X = {1, 2}
Y = {1, 2, 3}
Z = {4, 5}

X.issubset(Y)                               # True (all X in Y)
Y.issuperset(X)                             # True (Y contains all X)
X.isdisjoint(Z)                             # True (no common elements)

# Membership (FAST O(1) lookup!)
2 in A                                      # True
7 not in A                                  # True

# Size and copy
len(A)                                      # Number of elements
copy_of_A = A.copy()                        # Shallow copy

# === SET COMPREHENSION ===

# Basic: {expression for item in iterable}
squares = {x**2 for x in range(5)}          # {0, 1, 4, 9, 16}

# With condition
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# From list with transformation
words = ["hello", "world", "python"]
lengths = {len(word) for word in words}     # {5, 6} (sets remove duplicates!)

# === PRACTICAL PATTERNS ===

# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 4, 4, 4]
unique = list(set(numbers))                 # [1, 2, 3, 4] (order may change!)

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)            # {4, 5}

# Check if all required items are present
required = {"ID", "name", "email"}
user_data = {"name": "John", "email": "john@example.com"}
missing = required - set(user_data.keys())  # {"ID"}

# Count unique items
text = "hello world hello python"
unique_words = len(set(text.split()))       # 3 ("hello", "world", "python")