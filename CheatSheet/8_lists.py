# === Lists ===

# === Creation and Basics ===

# 4 Ways to create lists
list1 = []                            # Empty
list2 = [1, 2, 3]                     # Literal  
list3 = list()                        # Constructor
list4 = list("hello")                 # From string → ['h','e','l','l','o']
list5 = [x*2 for x in range(5)]       # Comprehension → [0,2,4,6,8]

# Mixed types (Python allows everything!)
mixed = ["text", 42, 3.14, True, None, [1,2,3], {"key":"value"}]

# List of lists (2D/matrix)
matrix = [[1,2,3], [4,5,6], [7,8,9]]

# === Access and Slicing ===

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0-based)
fruits[0]      # "apple"   (1st)
fruits[2]      # "cherry"  (3rd)

# Negative indexing (from end)
fruits[-1]     # "elderberry" (last)
fruits[-2]     # "date"       (2nd last)

# Slicing [start:stop:step] (stop is EXCLUSIVE!)
fruits[1:3]    # ["banana", "cherry"]      (index 1 to 2)
fruits[:3]     # ["apple", "banana", "cherry"] (start to 2)
fruits[2:]     # ["cherry", "date", "elderberry"] (2 to end)
fruits[::2]    # ["apple", "cherry", "elderberry"] (every 2nd)
fruits[::-1]   # REVERSE list! ["elderberry","date","cherry","banana","apple"]

# Get portions
first_two = fruits[:2]      # First 2
last_two = fruits[-2:]      # Last 2
middle = fruits[1:-1]       # All except first/last

# === Modification Methods ===

nums = [1, 2, 3]

# ADD elements
nums.append(4)              # → [1,2,3,4] (add to end)
nums.insert(1, 1.5)         # → [1,1.5,2,3] (insert at index)
nums.extend([5,6,7])        # → [1,2,3,5,6,7] (add multiple)
nums += [8,9]               # Same as extend

# REMOVE elements
nums.remove(2)              # → [1,3] (remove by VALUE)
popped = nums.pop()         # → Remove last, get it (3)
popped = nums.pop(0)        # → Remove at index, get it (1)
del nums[1]                 # → Delete by index
del nums[1:3]               # → Delete slice
nums.clear()                # → [] (empty list)

# REORGANIZE
nums = [3,1,4,1,5,9,2]
nums.sort()                 # → [1,1,2,3,4,5,9] (ascending)
nums.sort(reverse=True)     # → [9,5,4,3,2,1,1] (descending)
nums.reverse()              # → [2,9,5,1,4,1,3] (just reverse order)

sorted_nums = sorted(nums)  # NEW sorted list (original unchanged)
reversed_nums = list(reversed(nums))  # NEW reversed list

# === Search and Info ===

nums = [1, 2, 3, 2, 4, 2]

# Basic info
len(nums)                   # 6 (length)
min(nums)                   # 1 (smallest)
max(nums)                   # 4 (largest)
sum(nums)                   # 14 (total)

# Searching
nums.index(2)               # 1 (first position of 2)
nums.index(2, 2)            # 3 (start searching from index 2)
nums.count(2)               # 3 (how many times 2 appears)

# Check existence
2 in nums                   # True
10 not in nums              # True

# Sorting with custom key
students = ["Alice", "Bob", "Charlie", "David"]
students.sort(key=len)  # Sort by length: ['Bob', 'Alice', 'David', 'Charlie']
students.sort(key=lambda x: x[-1])  # Sort by last character

# === List Comprehension === 

# Basic: [expression for item in iterable]
squares = [x**2 for x in range(5)]            # [0,1,4,9,16]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(10) if x%2==0]      # [0,2,4,6,8]

# Nested: [expression for sublist in list for item in sublist]
matrix = [[1,2],[3,4]]
flat = [num for row in matrix for num in row] # [1,2,3,4]

# With if-else: [true_expr if condition else false_expr for item]
labels = ["Even" if x%2==0 else "Odd" for x in range(5)]  # ["Even","Odd","Even","Odd","Even"]

# Dictionary comprehension from list
{x: x**2 for x in range(5)}                   # {0:0, 1:1, 2:4, 3:9, 4:16}