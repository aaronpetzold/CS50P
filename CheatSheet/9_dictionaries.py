# === Dictionaries === 

# === Creation & Basics ===

# 5 Ways to create dicts

dict1 = {}                                    # Empty
dict2 = {"name": "John", "age": 30}           # Literal
dict3 = dict()                                # Constructor
dict4 = dict(name="Alice", age=25)            # Keyword args (keys become strings!)
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

# Dict from two lists
keys = ["a","b","c"]
values = [1,2,3]
dict6 = dict(zip(keys, values))              # {"a":1, "b":2, "c":3}

# === Access & Modification ===

person = {"name": "John", "age": 30}

# Safe access (won't crash)
name = person.get("name")                    # "John"
city = person.get("city")                    # None (key doesn't exist)
city = person.get("city", "Unknown")         # "Unknown" (default)

# Unsafe access (crashes if key missing)
name = person["name"]                        # "John"
# city = person["city"]                      # ❌ KeyError!

# Set default if key missing
person.setdefault("city", "Berlin")          # Adds "city":"Berlin" if not exist

# Update multiple keys
person.update({"age": 31, "job": "Engineer", "city": "Hamburg"})

# Merge two dicts (Python 3.9+)
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2                       # {"a":1, "b":2}

# === Looping Techniques ===

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

# Loop through both (BEST)
for key, value in person.items():
    print(f"{key}: {value}")

# With enumerate (get index too)
for i, (key, value) in enumerate(person.items()):
    print(f"{i}. {key}: {value}")

# === Dictionary Comprehension ===

# Basic: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}        # {0:0, 1:1, 2:4, 3:9, 4:16}

# From list with index as key
fruits = ["apple", "banana", "cherry"]
fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}  # {0:"apple", 1:"banana", 2:"cherry"}

# With condition
even_squares = {x: x**2 for x in range(10) if x%2==0}      # {0:0, 2:4, 4:16, 6:36, 8:64}

# Transform existing dict
person = {"name": "john", "age": "30"}
upper_person = {k.upper(): v.upper() for k,v in person.items()}  # {"NAME":"JOHN", "AGE":"30"}

# Swap keys and values (if values are hashable)
inverted = {v: k for k, v in person.items()}

# === Useful Methods ===

person = {"name": "John", "age": 30, "city": "Berlin"}

# Copying
import copy
shallow_copy = person.copy()                # Shallow copy
deep_copy = copy.deepcopy(person)           # Need: import copy

# Removing
age = person.pop("age")                     # Remove key, return value
removed = person.pop("country", "N/A")      # Return default if key missing
key, value = person.popitem()               # Remove & return last (key,value)

# Views (update with original)
keys_view = person.keys()                   # dict_keys(['name','city'])
values_view = person.values()               # dict_values(['John','Berlin'])
items_view = person.items()                 # dict_items([('name','John'),('city','Berlin')])
