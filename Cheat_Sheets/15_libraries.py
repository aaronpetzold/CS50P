# === Libraries & APIs ===


# ========== TABLE OF CONTENTS ==========
#
# 1. IMPORTS (Basics)
# 2. sys (System & Command Line)
# 3. os (Operating System Interface)
# 4. subprocess (Run External Commands)
# 5. datetime (Dates & Times)
# 6. time (Sleep & Timers)
# 7. re (Regular Expressions)
# 8. json (API Data Format)
# 9. requests (HTTP & APIs)
# 10. collections (Advanced Data Structures)
# 11. itertools (Iteration Tools)
# 12. statistics (Basic Stats)
# 13. hashlib (Hashing for Security)
# 14. argparse (Professional CLI Tools)
# 15. Third-Party Libraries (pip install)
# 16. Creating Your Own Module
# 17. Creating Your Own Package
# 18. if __name__ == "__main__"
# 19. Managing Packages with pip
# 20. Quick Reference
#
# ========================================


# How to use Python's standard library, external APIs, and create your own modules/packages.


# === 1. IMPORTS (Basics) ===

# Import entire module
import math
print(math.sqrt(16))        # 4.0

# Import specific functions (no prefix)
from math import sqrt, pi
print(sqrt(25))             # 5.0

# Import with alias
import datetime as dt
today = dt.date.today()

# Import everything (NOT recommended – pollutes namespace)
# from os import *

# See what's in a module
import random
print(dir(random))          # List all names
help(random.choice)         # Show documentation



# === 2. sys (System & Command Line) ===

import sys

# Command-line arguments: python script.py arg1 arg2
script_name = sys.argv[0]           # "script.py"
first_arg = sys.argv[1] if len(sys.argv) > 1 else None
all_args = sys.argv[1:]             # List of arguments

# Exit program with status code (0 = success, 1+ = error)
if error_occurred:
    sys.exit(1)

# Python search path (where imports are looked for)
print(sys.path)                     # List of directories

# Version and platform
print(sys.version)                  # "3.14.0 ..."
print(sys.platform)                 # 'win32', 'linux', 'darwin'

# Standard streams (rarely needed, but powerful)
sys.stdout.write("Hello\n")         # Like print()
sys.stderr.write("Error!\n")        # For error messages

# Max recursion depth
sys.setrecursionlimit(2000)



# === 3. os (Operating System Interface) ===

import os

# Paths and directories
os.getcwd()                         # Current working directory
os.chdir("/path/to/folder")         # Change directory
os.listdir(".")                     # List files in current dir
os.path.exists("file.txt")          # Check if file/dir exists
os.path.isfile("file.txt")          # Is it a file?
os.path.isdir("folder")             # Is it a directory?
os.path.join("folder", "sub", "file.txt")   # Platform-safe path

# File operations
os.remove("temp.txt")               # Delete file
os.rename("old.txt", "new.txt")     # Rename
os.mkdir("new_folder")              # Create directory
os.rmdir("empty_folder")            # Remove empty directory

# Environment variables
print(os.environ.get("PATH"))       # Get environment variable
os.environ["MY_VAR"] = "value"      # Set (temporary)

# Run system command
os.system("echo Hello")             # Runs in shell (simple but limited)
# Better: use subprocess module



# === 4. subprocess (Run External Commands) ===

import subprocess

# Run command and get output
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)                # Standard output
print(result.stderr)                # Error output
print(result.returncode)            # 0 if success

# Run with shell (careful with user input)
subprocess.run("echo Hello", shell=True)



# === 5. datetime (Dates & Times) ===

import datetime as dt

# Dates
d = dt.date(2024, 12, 25)           # 2024-12-25
today = dt.date.today()
print(d.year, d.month, d.day)

# Times
t = dt.time(14, 30, 15)             # 14:30:15

# Datetime (combined)
now = dt.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # Format as string
parsed = dt.datetime.strptime("2024-01-01", "%Y-%m-%d")  # Parse string

# Timedelta (differences)
delta = dt.timedelta(days=7)
next_week = today + delta
age = now - parsed                  # Returns timedelta
print(age.days)                     # Number of days

# Common formats
# %Y = 2024, %m = 01, %d = 31, %H = 24h, %I = 12h, %M = minute, %S = second



# === 6. time (Sleep & Timers) ===

import time

# Sleep (pause execution)
time.sleep(2)                       # Pause 2 seconds

# Measure execution time
start = time.time()
# ... do work ...
elapsed = time.time() - start
print(f"Took {elapsed:.2f} seconds")



# === 7. re (Regular Expressions) ===

import re

text = "My email: alice@example.com"

# Search for pattern
match = re.search(r"[\w\.-]+@[\w\.-]+", text)
if match:
    print(match.group())            # "alice@example.com"

# Find all matches
numbers = re.findall(r"\d+", "12 apples, 34 oranges")  # ['12','34']

# Replace
cleaned = re.sub(r"\d+", "X", "Order 123")  # "Order X"

# Split by pattern
parts = re.split(r"\s+", "a  b   c")        # ['a','b','c']

# Common patterns:
# \d = digit, \w = word, \s = whitespace, . = anything, + = one or more, * = zero or more



# === 8. json (API Data Format) ===

import json

# Convert Python dict to JSON string
data = {"name": "Alice", "age": 30, "hobbies": ["reading", "coding"]}
json_string = json.dumps(data)              # '{"name": "Alice", ...}'
pretty = json.dumps(data, indent=2)         # Pretty print

# Convert JSON string back to Python
json_str = '{"name": "Bob", "age": 25}'
parsed = json.loads(json_str)               # {"name": "Bob", "age": 25}

# Read JSON from file
with open("data.json", "r") as f:
    loaded = json.load(f)

# Write JSON to file
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)



# === 9. requests (HTTP & APIs) ===

# Install: pip install requests
import requests

# --- GET Request (Read) ---
response = requests.get("https://api.github.com/users/octocat")

# Check status
print(response.status_code)                 # 200 = OK
print(response.ok)                          # True if status < 400

# Get data
user = response.json()                      # Parse JSON → dict
print(user["name"])                         # "The Octocat"
print(user["followers"])

# Raw response (for non-JSON)
print(response.text)                        # String
print(response.content)                     # Bytes (for images)

# Headers
print(response.headers['content-type'])

# --- GET with Parameters ---
params = {"q": "python", "per_page": 5}
response = requests.get("https://api.github.com/search/repositories", params=params)
results = response.json()
for repo in results["items"]:
    print(repo["name"])

# --- POST Request (Create) ---
new_post = {"title": "My Post", "body": "Hello World"}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(response.status_code)                 # 201 Created
print(response.json()["id"])                # New ID

# --- PUT (Update) & DELETE ---
update = {"title": "Updated"}
requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update)
requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# --- Headers & Authentication ---
headers = {"User-Agent": "MyApp/1.0", "Authorization": "token YOUR_TOKEN"}
response = requests.get("https://api.github.com/user", headers=headers)

# --- Error Handling ---
try:
    response = requests.get("https://api.github.com/user", timeout=5)
    response.raise_for_status()             # Raises exception for 4xx/5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Other error: {e}")

# --- Session (persistent cookies) ---
session = requests.Session()
session.headers.update({"User-Agent": "MyApp/1.0"})
session.post("https://example.com/login", json={"user": "alice", "pass": "secret"})
dashboard = session.get("https://example.com/dashboard")   # Uses same session

# --- Practical API Examples ---

# 1. Get random joke
resp = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = resp.json()
print(f"{joke['setup']} - {joke['punchline']}")

# 2. Download image
resp = requests.get("https://example.com/image.jpg")
with open("image.jpg", "wb") as f:
    f.write(resp.content)

# 3. Weather (needs API key)
# API_KEY = "your_key"
# url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"
# resp = requests.get(url)
# print(resp.json()["main"]["temp"])



# === 10. collections (Advanced Data Structures) ===

from collections import Counter, defaultdict, namedtuple, deque

# Counter – count occurrences
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(fruits)
print(counts.most_common(2))    # [('apple',3), ('banana',2)]

# defaultdict – missing keys return default
d = defaultdict(int)            # int default = 0
d["count"] += 1                 # No KeyError

d2 = defaultdict(list)          # list default = []
d2["colors"].append("red")

# namedtuple – lightweight class
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)

# deque – fast append/pop from both ends
q = deque([1, 2, 3])
q.appendleft(0)                 # [0,1,2,3]
q.popleft()                     # 0



# === 11. itertools (Iteration Tools) ===

from itertools import chain, cycle, product, combinations, permutations

# chain – flatten sequences
list(chain([1,2], [3,4]))       # [1,2,3,4]

# cycle – infinite iterator
c = cycle(["A","B","C"])
next(c)                         # 'A', next 'B', next 'C', then 'A' again

# product – Cartesian product
list(product([1,2], [3,4]))     # [(1,3),(1,4),(2,3),(2,4)]

# combinations – all combinations of length k
list(combinations([1,2,3], 2))  # [(1,2),(1,3),(2,3)]

# permutations – all orders
list(permutations([1,2,3], 2))  # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]



# === 12. statistics (Basic Stats) ===

import statistics

data = [10, 20, 30, 40, 50]
statistics.mean(data)           # 30
statistics.median(data)         # 30
statistics.stdev(data)          # ~15.81 (standard deviation)



# === 13. hashlib (Hashing for Security) ===

import hashlib

text = b"Hello, World!"         # Must be bytes
hash_obj = hashlib.sha256(text)
hex_digest = hash_obj.hexdigest()   # 64-character hex string

# Common use: password hashing (never store plain text!)
password = "mysecret".encode()
hashed = hashlib.sha256(password).hexdigest()



# === 14. argparse (Professional CLI Tools) ===

import argparse

parser = argparse.ArgumentParser(description="My awesome script")
parser.add_argument("--input", "-i", required=True, help="Input file")
parser.add_argument("--output", "-o", help="Output file")
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose")
args = parser.parse_args()

# Use args.input, args.output, args.verbose
if args.verbose:
    print(f"Reading {args.input}")

# Run script: python script.py --input data.txt --verbose



# === 15. Third-Party Libraries (pip install) ===

# ---- requests (already covered) ----
# pip install requests

# ---- pandas (data analysis) ----
# import pandas as pd
# df = pd.read_csv("data.csv")
# print(df.head())

# ---- numpy (numerical arrays) ----
# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr.mean())

# ---- flask (web framework) ----
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def home(): return "Hello"
# app.run()

# ---- beautifulsoup4 (web scraping) ----
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")



# === 16. Creating Your Own Module ===

# A module is a single .py file.
# Save as mymodule.py:
"""
def greet(name):
    return f"Hello {name}!"

def add(a, b):
    return a + b
"""

# Then in another file:
import mymodule
print(mymodule.greet("Alice"))
from mymodule import add
print(add(2, 3))



# === 17. Creating Your Own Package ===

# A package is a directory with an __init__.py file.
# Directory structure:
"""
mypackage/
    __init__.py          # Makes folder a package
    core.py
    utils.py
"""

# mypackage/core.py
"""
def process(data):
    return data.upper()
"""

# mypackage/utils.py
"""
def helper(x):
    return x * 2
"""

# mypackage/__init__.py (expose selected functions at package level)
"""
from .core import process
from .utils import helper

__all__ = ["process", "helper"]   # for "from mypackage import *"
"""

# --- Using the Package ---
import mypackage
mypackage.process("hello")   # "HELLO"

# Or import specific
from mypackage import process, helper
process("hi")

# --- What __init__.py Can Do ---
# 1. Make a directory importable (required before Python 3.3)
# 2. Initialize package (set variables, load config)
# 3. Control what gets imported with `from package import *` (via __all__)
# 4. Shorten import paths (expose inner modules at top level)

# Example __init__.py with initialization:
"""
print(f"Loading {__name__}...")
VERSION = "1.0.0"

from .core import main_function

__all__ = ["main_function", "VERSION"]
"""

# --- Importing Within a Package (Relative Imports) ---
# Inside mypackage/submodule.py:
# from .core import some_func       # sibling module
# from ..parent import parent_func  # go up one level

# --- __pycache__ ---
# Python caches compiled bytecode here. Safe to delete, will be regenerated.



# === 18. if __name__ == "__main__" ===

# Prevents code from running when module/package is imported.
def main():
    # Test or main code
    pass

if __name__ == "__main__":
    main()



# === 19. Managing Packages with pip ===

# List installed packages: pip list
# Install: pip install package_name
# Uninstall: pip uninstall package_name
# Freeze to file: pip freeze > requirements.txt
# Install from file: pip install -r requirements.txt

# Install your own package in development mode (editable)
# Create setup.py in parent folder:
"""
from setuptools import setup, find_packages
setup(name="mypackage", version="0.1", packages=find_packages())
"""
# Then: pip install -e .   (changes reflect immediately)



# === 20. Quick Reference ===
# | Library      | Purpose               | Key Functions                        |
# |--------------|-----------------------|--------------------------------------|
# | sys          | System/CLI            | argv, exit, path                     |
# | os           | OS operations         | getcwd, listdir, path.join           |
# | subprocess   | Run commands          | run                                  |
# | datetime     | Dates/times           | date, datetime, timedelta            |
# | time         | Sleep/timers          | sleep, time                          |
# | re           | Regex                 | search, findall, sub                 |
# | json         | Parse JSON            | loads, dumps, load, dump             |
# | requests     | HTTP calls            | get, post, put, delete               |
# | collections  | Data structures       | Counter, defaultdict, deque          |
# | itertools    | Iteration tools       | chain, product, combinations         |
# | statistics   | Math stats            | mean, median, stdev                  |
# | hashlib      | Hashing               | sha256, hexdigest                    |
# | argparse     | CLI arguments         | ArgumentParser                       |