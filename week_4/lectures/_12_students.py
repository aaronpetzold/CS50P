# === PEP 8 & Code Style ===

# PEP 8 = Python's official style guide (makes code readable and consistent)

# === Key PEP 8 Rules ===

# Indentation: 4 spaces per level (not tabs!)
if True:
    print("4 spaces here")

# Line length: maximum 79 characters (72 for docstrings)
# Bad: very long line with more than 79 characters that goes on and on...
# Good:
long_variable = "This line is split"
long_variable += " into multiple lines"

# Blank lines:
# - 2 blank lines between functions
# - 1 blank line between methods in a class
# - 1 blank line before return statements for clarity

def function_one():
    pass


def function_two():
    pass

# Spaces around operators:
x = 5 + 3          # ✅ Spaces around operators
x = 5+3            # ❌ No spaces

# No spaces inside parentheses:
spam(ham[1], {eggs: 2})   # ✅
spam( ham[ 1 ], { eggs: 2 } )  # ❌

# Comments: start with # and one space
# This is a good comment

# Naming conventions:
# - variables/functions: snake_case → my_variable, calculate_total()
# - classes: PascalCase → MyClass, StudentRecord
# - constants: UPPER_CASE → MAX_SIZE, PI
# - private attributes: _leading_underscore → _internal_method()


# === Black (The "Opinionated" Formatter) ===

# Black formats code automatically to follow PEP 8
# Install: pip install black

# Before Black:
students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}
for student in students:
  print(student)      # ❌ 2 spaces (should be 4)

# After running: black myfile.py
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student)      # ✅ 4 spaces

# Black fixes:
# - indentation (converts tabs/mixed to 4 spaces)
# - line length (splits long lines)
# - spaces around operators
# - trailing commas
# - consistent quotes (double quotes by default)
# - removes trailing whitespace

# Black commands:
# black myfile.py         → format single file
# black .                 → format all .py files in folder
# black --check .         → check if files need formatting (no changes)
# black --diff myfile.py  → preview changes without saving

# VS Code integration (settings.json):
# "python.formatting.provider": "black",
# "editor.formatOnSave": true


# === Other Style Tools ===

# flake8 - linter (finds style errors)
# pip install flake8
# flake8 myfile.py

# isort - sorts imports alphabetically
# pip install isort
# isort myfile.py

# Before isort:
# import sys
# import os
# from math import sqrt
# import json

# After isort:
# import json
# import os
# import sys
# from math import sqrt


# === Quick Reference ===
# | Rule                    | Good                     | Bad                    |
# |-------------------------|--------------------------|------------------------|
# | Indentation             | 4 spaces                 | tabs or 2 spaces       |
# | Max line length         | ≤ 79 chars               | 80+ chars              |
# | Spaces around =         | x = 5                    | x=5                    |
# | Function names          | calculate_total()        | CalculateTotal()       |
# | Class names             | StudentRecord            | student_record         |
# | Constant names          | MAX_SIZE                 | max_size               |
# | Blank lines between func| 2 lines                  | 1 line                 |
# | Comments                | # This is a comment      | #This is bad           |