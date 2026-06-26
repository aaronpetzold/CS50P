# === Dictionaries ===


# ========== TABLE OF CONTENTS ==========
#
# 1. CREATION (5 ways)
# 2. ACCESS AND MODIFICATION
# 3. LOOPING TECHNIQUES
# 4. DICTIONARY COMPREHENSION
# 5. USEFUL METHODS (pop, popitem, copy, etc.)
# 6. VIEWS (keys, values, items)
# 7. MERGING (| operator, update)
#
# ========================================


# Definition: Dictionaries store key-value pairs. Keys must be immutable and unique,
# values can be any type. They are unordered (prior to Python 3.7) / insertion‑ordered (3.7+).


# ---------- 1. CREATION (5 ways) ----------

dict1 = {}                                    # Empty
dict2 = {"name": "John", "age": 30}           # Literal
dict3 = dict()                                # Constructor
dict4 = dict(name="Alice", age=25)            # Keyword arguments (keys become strings)
dict5 = dict([("name","Bob"), ("age",35)])    # From list of tuples

# Nested dictionaries
person = {
    "name": "Emma",
    "age": 28,
    "address": {
        "street": "Main St",
        "city": "Berlin",
        "zip": "10115"
    },
    "hobbies": ["reading", "hiking", "coding"]
}

# From two lists
keys = ["a","b","c"]
values = [1,2,3]
dict6 = dict(zip(keys, values))              # {"a":1, "b":2, "c":3}


# ---------- 2. ACCESS AND MODIFICATION ----------

person = {"name": "John", "age": 30}

# Safe access (no KeyError)
name = person.get("name")                    # "John"
city = person.get("city")                    # None
city = person.get("city", "Unknown")         # "Unknown" (default)

# Unsafe access (raises KeyError if missing)
name = person["name"]                        # "John"
# city = person["city"]                      # KeyError!

# Set default if key missing (in-place)
person.setdefault("city", "Berlin")          # adds "city":"Berlin" only if not present

# Update multiple keys (in‑place)
person.update({"age": 31, "job": "Engineer", "city": "Hamburg"})

# Merge two dicts (Python 3.9+)
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2                       # {"a":1, "b":2}
dict1 |= dict2                               # update dict1 in‑place


# ---------- 3. LOOPING TECHNIQUES ----------

person = {"name": "John", "age": 30, "city": "Berlin"}

# Loop through keys (default)
for key in person:
    print(key, person[key])

# Explicit keys
for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through both (most common)
for key, value in person.items():
    print(f"{key}: {value}")

# With index (enumerate)
for i, (key, value) in enumerate(person.items()):
    print(f"{i}. {key}: {value}")


# ---------- 4. DICTIONARY COMPREHENSION ----------

# Basic: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}        # {0:0, 1:1, 2:4, 3:9, 4:16}

# From list with index as key
fruits = ["apple", "banana", "cherry"]
fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}  # {0:"apple",1:"banana",2:"cherry"}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}  # {0:0,2:4,4:16,6:36,8:64}

# Transform existing dict
person = {"name": "john", "age": "30"}
upper_person = {k.upper(): v.upper() for k, v in person.items()}  # {"NAME":"JOHN","AGE":"30"}

# Swap keys and values (if values are hashable)
inverted = {v: k for k, v in person.items()}  # {"john":"name","30":"age"}


# ---------- 5. USEFUL METHODS (pop, popitem, copy, etc.) ----------

person = {"name": "John", "age": 30, "city": "Berlin"}

# Copying
shallow_copy = person.copy()                 # shallow copy (new dict, same objects)
import copy
deep_copy = copy.deepcopy(person)            # deep copy (recursive)

# Removing
age = person.pop("age")                      # removes key, returns value (30)
removed = person.pop("country", "N/A")       # returns default if key missing
key, value = person.popitem()                # removes and returns last inserted (key,value)

# Other
len(person)                                  # number of keys
"name" in person                             # True (key membership)
"city" not in person                         # False after popitem?


# ---------- 6. VIEWS (keys, values, items) ----------

# Views are dynamic – they reflect changes to the original dict.
person = {"name": "John", "age": 30}
keys_view = person.keys()                    # dict_keys(['name','age'])
values_view = person.values()                # dict_values(['John',30])
items_view = person.items()                  # dict_items([('name','John'),('age',30)])

# Convert to list if needed
keys_list = list(person.keys())

# Views update when dict changes
person["city"] = "Berlin"
print(keys_view)                             # dict_keys(['name','age','city'])


# ---------- 7. MERGING (| operator, update) ----------

# Using | (Python 3.9+)
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = a | b                               # {'x':1, 'y':3, 'z':4} (b overwrites a)
a |= b                                       # update a in‑place

# Using update() – works in all Python versions
a.update(b)                                  # same effect

# Using ** unpacking (older style)
merged = {**a, **b}