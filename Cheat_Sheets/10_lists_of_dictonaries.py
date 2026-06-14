# === List of Dictionaries (Database‑like Structure) ===


# ========== TABLE OF CONTENTS ==========
#
# 1. CREATING A LIST OF DICTIONARIES
# 2. ACCESSING ELEMENTS (by index and key)
# 3. LOOPING THROUGH ALL ROWS
# 4. SEARCHING FOR A SPECIFIC ITEM
# 5. ADDING A NEW ROW (APPEND)
# 6. MODIFYING (ADDING NEW FIELDS)
# 7. SORTING BY A SPECIFIC FIELD (lambda)
# 8. FILTERING WITH LIST COMPREHENSION
# 9. GROUPING WITH defaultdict
#
# ========================================


# Definition: A list of dictionaries is a common way to represent tabular data (like a database table).
# Each dictionary is a row; keys are column names, values are cell contents.


# ---------- 1. CREATING A LIST OF DICTIONARIES ----------

students = [
    {"name": "Hermione", "house": "Gryffindor", "year": 5},
    {"name": "Harry", "house": "Gryffindor", "year": 5},
    {"name": "Draco", "house": "Slytherin", "year": 5},
    {"name": "Luna", "house": "Ravenclaw", "year": 4}
]


# ---------- 2. ACCESSING ELEMENTS (by index and key) ----------

# Access the whole dictionary of the second student (index 1)
harry = students[1]                           # {"name": "Harry", "house": "Gryffindor", "year": 5}

# Access a specific field (value) inside that dictionary
harry_house = students[1]["house"]            # "Gryffindor"


# ---------- 3. LOOPING THROUGH ALL ROWS ----------

for student in students:
    print(f"{student['name']} is in {student['house']}")


# ---------- 4. SEARCHING FOR A SPECIFIC ITEM ----------

for student in students:
    if student["name"] == "Hermione":
        print(f"Found: {student}")


# ---------- 5. ADDING A NEW ROW (APPEND) ----------

students.append({"name": "Neville", "house": "Gryffindor", "year": 5})


# ---------- 6. MODIFYING (ADDING NEW FIELDS) ----------

# Add a new key‑value pair to a specific row.
for student in students:
    if student["name"] == "Harry":
        student["patronus"] = "Stag"           # Adds field "patronus" with value "Stag"


# ---------- 7. SORTING BY A SPECIFIC FIELD (lambda) ----------

# Sort in‑place by name (alphabetically)
students.sort(key=lambda s: s["name"])

# Sort in‑place by year (numerically)
students.sort(key=lambda s: s["year"])

# To create a new sorted list without modifying the original:
sorted_by_name = sorted(students, key=lambda s: s["name"])


# ---------- 8. FILTERING WITH LIST COMPREHENSION ----------

# Create a new list containing only Gryffindor students.
gryffindors = [s for s in students if s["house"] == "Gryffindor"]


# ---------- 9. GROUPING WITH defaultdict ----------

from collections import defaultdict

# Group students by house, collecting their names.
houses = defaultdict(list)          # default value for missing keys is an empty list

for student in students:
    houses[student["house"]].append(student["name"])

# After the loop, houses["Gryffindor"] is a list of all Gryffindor names.
print(houses["Gryffindor"])

# Without defaultdict you would need to check for key existence manually:
# if house not in groups: groups[house] = []