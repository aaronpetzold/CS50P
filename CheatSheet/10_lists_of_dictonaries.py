# Database-like structure
students = [
    {"name": "Hermione", "house": "Gryffindor", "year": 5},
    {"name": "Harry", "house": "Gryffindor", "year": 5},
    {"name": "Draco", "house": "Slytherin", "year": 5},
    {"name": "Luna", "house": "Ravenclaw", "year": 4}
]

# Access
harry = students[1]                           # Get Harry's dict
harry_house = students[1]["house"]            # Get specific field

# Loop through all
for student in students:
    print(f"{student['name']} is in {student['house']}")

# Search
for student in students:
    if student["name"] == "Hermione":
        print(f"Found: {student}")

# Add new student
students.append({"name": "Neville", "house": "Gryffindor", "year": 5})

# Modify
for student in students:
    if student["name"] == "Harry":
        student["patronus"] = "Stag"          # Add new field

# Sort by specific field
students.sort(key=lambda s: s["name"])  # Sort alphabetically by name
students.sort(key=lambda s: s["year"])  # Sort by year

# Filter with list comprehension
gryffindors = [s for s in students if s["house"] == "Gryffindor"]

# Group by field 
from collections import defaultdict
houses = defaultdict(list)
for student in students:
    houses[student["house"]].append(student["name"])