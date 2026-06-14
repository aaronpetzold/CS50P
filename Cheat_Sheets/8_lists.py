# === Lists ===


# ========== TABLE OF CONTENTS ==========
#
# 1. CREATION
# 2. ACCESS AND SLICING
# 3. MODIFICATION (ADDING, REMOVING)
# 4. SORTING AND REVERSING
# 5. SEARCHING AND INFORMATION
# 6. LIST COMPREHENSION
# 7. ADDITIONAL METHODS (copy, index with bounds)
# 8. LIST OPERATIONS (concatenation, repetition)
#
# ========================================


# Definition: Lists are ordered, mutable, and can contain elements of any type.
# They are one of the most commonly used data structures in Python.


# ---------- 1. CREATION ----------

# Empty list
list1 = []

# Literal
list2 = [1, 2, 3]

# Constructor
list3 = list()

# From any iterable (string → characters)
list4 = list("hello")               # ['h','e','l','l','o']

# List comprehension
list5 = [x*2 for x in range(5)]     # [0,2,4,6,8]

# Mixed types allowed
mixed = ["text", 42, 3.14, True, None, [1,2,3], {"key":"value"}]

# List of lists (matrix)
matrix = [[1,2,3], [4,5,6], [7,8,9]]


# ---------- 2. ACCESS AND SLICING ----------

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0‑based)
fruits[0]       # "apple"
fruits[2]       # "cherry"

# Negative indexing (from the end)
fruits[-1]      # "elderberry"
fruits[-2]      # "date"

# Slicing [start:stop:step] (stop is exclusive)
fruits[1:3]     # ["banana", "cherry"]      (indices 1,2)
fruits[:3]      # ["apple", "banana", "cherry"]
fruits[2:]      # ["cherry", "date", "elderberry"]
fruits[::2]     # ["apple", "cherry", "elderberry"] (every 2nd)
fruits[::-1]    # reverse: ["elderberry","date","cherry","banana","apple"]

# Get portions
first_two = fruits[:2]
last_two = fruits[-2:]
middle = fruits[1:-1]               # all except first and last


# ---------- 3. MODIFICATION (ADDING, REMOVING) ----------

nums = [1, 2, 3]

# Adding
nums.append(4)                      # → [1,2,3,4] (add to end)
nums.insert(1, 1.5)                 # → [1,1.5,2,3] (insert at index)
nums.extend([5,6,7])                # → [1,2,3,5,6,7] (add multiple)
nums += [8,9]                       # same as extend

# Removing
nums.remove(2)                      # removes first occurrence of value 2
popped = nums.pop()                 # removes and returns last element (3)
popped = nums.pop(0)                # removes and returns element at index 0
del nums[1]                         # delete by index
del nums[1:3]                       # delete slice
nums.clear()                        # empty the list


# ---------- 4. SORTING AND REVERSING ----------

nums = [3,1,4,1,5,9,2]

# In-place methods (modify the original list)
nums.sort()                         # ascending → [1,1,2,3,4,5,9]
nums.sort(reverse=True)             # descending → [9,5,4,3,2,1,1]
nums.reverse()                      # reverse order → [2,9,5,1,4,1,3]

# Functions that return a new list (original unchanged)
sorted_nums = sorted(nums)          # ascending (new list)
reversed_nums = list(reversed(nums)) # reversed (new list)

# Sorting with custom key
students = ["Alice", "Bob", "Charlie", "David"]
students.sort(key=len)              # sort by length: ['Bob','Alice','David','Charlie']
students.sort(key=lambda x: x[-1])  # sort by last character


# ---------- 5. SEARCHING AND INFORMATION ----------

nums = [1, 2, 3, 2, 4, 2]

# Basic info
len(nums)                           # 6
min(nums)                           # 1
max(nums)                           # 4
sum(nums)                           # 14

# Searching
nums.index(2)                       # 1 (first occurrence)
nums.index(2, 2)                    # 3 (start search at index 2)
nums.count(2)                       # 3 (how many times 2 appears)

# Membership checks
2 in nums                           # True
10 not in nums                      # True

# Copying (shallow copy)
copy1 = nums.copy()                 # method
copy2 = nums[:]                     # slice
copy3 = list(nums)                  # constructor


# ---------- 6. LIST COMPREHENSION ----------

# Basic form: [expression for item in iterable]
squares = [x**2 for x in range(5)]          # [0,1,4,9,16]

# With condition: [expr for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]

# Nested loops: for sublist in matrix for item in sublist
matrix = [[1,2], [3,4]]
flat = [num for row in matrix for num in row]  # [1,2,3,4]

# With if‑else (ternary inside expression)
labels = ["Even" if x%2==0 else "Odd" for x in range(5)]
# ["Even","Odd","Even","Odd","Even"]

# Dictionary comprehension from list
{x: x**2 for x in range(5)}                  # {0:0,1:1,2:4,3:9,4:16}


# ---------- 7. ADDITIONAL METHODS (copy, index with bounds) ----------

# index() can take start and end parameters
nums = [10, 20, 30, 20, 40]
nums.index(20)                      # 1 (first)
nums.index(20, 2)                   # 3 (search from index 2)
nums.index(20, 2, 4)                # raises ValueError (not in slice)

# copy() – shallow copy (already mentioned in section 5)
# extend() vs append(): extend adds multiple items, append adds one item as a single element.

# pop() with negative index
nums.pop(-2)                        # removes the second last element


# ---------- 8. LIST OPERATIONS (concatenation, repetition) ----------

# Concatenation (+)
a = [1, 2]
b = [3, 4]
c = a + b                           # [1,2,3,4]

# Repetition (*)
zeros = [0] * 5                     # [0,0,0,0,0]
matrix_row = [[0]*3 for _ in range(2)]   # [[0,0,0],[0,0,0]] (safe repetition)

# Warning: [0]*3 creates a list of three zeros, but [[0]*3]*2 creates a list of two references to the same inner list.