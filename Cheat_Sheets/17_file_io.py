# === File Input/Output (File I/O) ===


# ========== TABLE OF CONTENTS ==========
#
# 1. OPENING A FILE
# 2. READING FILES
# 3. WRITING FILES
# 4. WORKING WITH PATHS (os, pathlib, glob, shutil)
# 5. BINARY FILES
# 6. FILE MODES CHEAT SHEET
# 7. COMMON PATTERNS
# 8. EXCEPTION HANDLING WITH FILES
# 9. CSV FILES
# 10. JSON FILES
# 11. PICKLE (Object Serialization)
# 12. IN-MEMORY FILES (StringIO, BytesIO)
# 13. WORKING WITH ARCHIVES (zipfile, tarfile)
# 14. TEMPORARY FILES AND DIRECTORIES
# 15. READING LARGE FILES IN CHUNKS
# 16. FILE PERMISSIONS AND METADATA
# 17. QUICK REFERENCE
#
# ========================================


# Definition: File I/O is the process of reading data from and writing data to files on disk.
# A file object is Python's connection to a file on your computer.


# ---------- 1. OPENING A FILE ----------

# Definition: Opening a file creates a file object that allows you to read from or write to that file.
# The open() function takes a filename and a mode. The mode tells Python what you want to do with the file.

# Modes explained (add 'b' for binary, 't' for text – default is text):
# "r" : Read mode. The file must already exist. You can only read, not write.
# "w" : Write mode. Creates a new file or overwrites an existing file. You can only write, not read.
# "a" : Append mode. Creates a new file or adds to the end of an existing file.
# "x" : Exclusive creation mode. Creates a new file but fails if the file already exists.
# "b" : Binary mode. Use with another mode (e.g., "rb" for read binary).
# "t" : Text mode. This is the default. Use with another mode (e.g., "rt" means read text).
# "+" : Read and write mode. Use with another mode (e.g., "r+" means read and write).

# Encoding (important for text files)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Basic open (you must close manually)
file = open("data.txt", "r")
content = file.read()
file.close()  # Always close to free system resources

# Better: 'with' statement (auto-closes even if errors occur)
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed when the indented block ends

# Custom context manager (for completeness)
class ManagedFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# ---------- 2. READING FILES ----------

# Definition: Reading a file means loading its contents from disk into memory as a string or list.

# Assume "example.txt" contains these three lines:
# Line 1
# Line 2
# Line 3

# read() - returns entire file as a single string
with open("example.txt", "r") as f:
    content = f.read()
    # content = "Line 1\nLine 2\nLine 3\n"

# readlines() - returns list of lines (each line includes the newline character)
with open("example.txt", "r") as f:
    lines = f.readlines()
    # lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

# readline() - returns one line at a time (includes newline)
with open("example.txt", "r") as f:
    line1 = f.readline()   # "Line 1\n"
    line2 = f.readline()   # "Line 2\n"

# Iterate over file object - most memory-efficient for large files
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the newline character

# read(n) - reads at most n characters (or bytes in binary mode)
with open("example.txt", "r") as f:
    first_5 = f.read(5)   # "Line "

# tell() - returns current position in file (bytes from start)
# seek() - moves to a specific position
with open("example.txt", "r") as f:
    print(f.tell())      # current position
    f.seek(10)           # move to byte 10
    data = f.read(20)    # read 20 characters

# Reading from the end (seek from end)
with open("example.txt", "rb") as f:
    f.seek(-10, 2)       # 2 = os.SEEK_END, move 10 bytes before end
    last_bytes = f.read()


# ---------- 3. WRITING FILES ----------

# Definition: Writing to a file means sending data from memory to be stored on disk.

# Write mode ("w") - overwrites entire file or creates new file
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")   # write() adds a single string
    f.write("Second line.")

# writelines() - writes multiple strings (does NOT add newlines automatically)
lines = ["apple\n", "banana\n", "cherry"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)   # Each string must already contain \n if you want new lines

# Append mode ("a") - adds to end of file without deleting existing content
with open("log.txt", "a") as f:
    f.write("New log entry\n")

# Writing with encoding
with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write("Café\n")


# ---------- 4. WORKING WITH PATHS (os, pathlib, glob, shutil) ----------

# Definition: A path is the location of a file or folder in your computer's file system.

import os
from pathlib import Path

# exists() - checks whether a file or folder exists
if os.path.exists("data.txt"):
    print("File exists")

# getcwd() - returns the current working directory (where your script is running)
cwd = os.getcwd()   # e.g., "/home/user/project"

# path.join() - combines folder and file names with the correct separator for your OS
full_path = os.path.join("folder", "subfolder", "file.txt")

# getsize() - returns file size in bytes
size = os.path.getsize("data.txt")

# rename() - changes a file's name
os.rename("old.txt", "new.txt")

# remove() - deletes a file permanently
os.remove("temp.txt")

# Additional os.path functions
os.path.basename("/path/to/file.txt")   # "file.txt"
os.path.dirname("/path/to/file.txt")    # "/path/to"
os.path.splitext("file.txt")            # ("file", ".txt")

# Pathlib (modern, object-oriented way)
p = Path("data.txt")
p.exists()               # True if file exists
p.read_text()            # Read entire file as string
p.write_text("content")  # Write string to file
p.stem                   # Filename without extension: "data"
p.suffix                 # Extension: ".txt"
p.parent                 # Parent directory path
p.name                   # Full filename: "data.txt"
p.resolve()              # Absolute path
p.mkdir(parents=True, exist_ok=True)   # Create directory and parents

# os.walk() - traverse directories recursively
for root, dirs, files in os.walk("my_folder"):
    for file in files:
        print(os.path.join(root, file))

# glob - find files by pattern
import glob
for py_file in glob.glob("**/*.py", recursive=True):
    print(py_file)

# shutil - high-level file operations
import shutil
shutil.copy("src.txt", "dst.txt")        # copy file
shutil.copy2("src.txt", "dst.txt")       # copy with metadata
shutil.move("old.txt", "new.txt")        # move/rename
shutil.rmtree("folder")                  # delete folder with contents
shutil.make_archive("backup", "zip", "folder")  # create zip archive
shutil.disk_usage("/")                   # total, used, free bytes


# ---------- 5. BINARY FILES ----------

# Definition: Binary files contain raw bytes (not human-readable text), such as images, audio, or executables.
# Binary mode prevents Python from trying to decode the bytes as text.

# Read binary file ("rb" mode)
with open("image.jpg", "rb") as f:
    data = f.read()   # Returns bytes object, not string

# Write binary file ("wb" mode)
with open("copy.jpg", "wb") as f:
    f.write(data)     # Writes bytes directly

# Read and write binary in chunks (memory efficient)
with open("large.bin", "rb") as src, open("copy.bin", "wb") as dst:
    while chunk := src.read(8192):
        dst.write(chunk)


# ---------- 6. FILE MODES CHEAT SHEET ----------

# | Mode | Description                          | File must exist | Overwrites? |
# |------|--------------------------------------|----------------|-------------|
# | "r"  | Read only (text)                     | Yes            | N/A         |
# | "w"  | Write (text, overwrites)             | No (creates)   | Yes         |
# | "a"  | Append (text, adds to end)           | No (creates)   | No          |
# | "x"  | Exclusive creation (fails if exists) | No             | N/A         |
# | "rb" | Read binary                          | Yes            | N/A         |
# | "wb" | Write binary                         | No (creates)   | Yes         |
# | "ab" | Append binary                        | No (creates)   | No          |
# | "r+" | Read and write (starts at beginning) | Yes            | Partial     |
# | "w+" | Read and write (overwrites)          | No (creates)   | Yes         |
# | "a+" | Read and append (starts at end)      | No (creates)   | No          |


# ---------- 7. COMMON PATTERNS ----------

# Copy a file: read from source, write to destination
with open("source.txt", "r") as src:
    content = src.read()
with open("dest.txt", "w") as dst:
    dst.write(content)

# Count lines in a file
with open("data.txt", "r") as f:
    line_count = sum(1 for _ in f)   # Counts each line

# Read last N lines (like the Unix 'tail' command)
from collections import deque
with open("log.txt", "r") as f:
    last_10_lines = deque(f, maxlen=10)   # Keeps only last 10 lines

# Search for a keyword in a file
with open("data.txt", "r") as f:
    for line in f:
        if "keyword" in line:
            print(line.strip())
            break

# Safe write: write to temporary file, then replace original
import tempfile
with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
    tmp.write("new content")
    tmp_path = tmp.name
os.replace(tmp_path, "data.txt")   # Atomic replace (no partial writes)

# Multiple files in one 'with'
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())

# Reading a file backwards (last line first) – using seek
with open("data.txt", "rb") as f:
    f.seek(0, os.SEEK_END)
    pos = f.tell()
    while pos > 0:
        pos -= 1
        f.seek(pos)
        if f.read(1) == b'\n':
            line = f.readline()
            print(line.decode().rstrip())


# ---------- 8. EXCEPTION HANDLING WITH FILES ----------

# Definition: File operations can fail for many reasons; exception handling lets you respond gracefully.

try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You don't have permission to read this file")
except UnicodeDecodeError as e:
    print(f"Encoding error: {e}")
except IOError as e:
    print(f"Input/output error: {e}")

# Using else and finally
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    content = f.read()
    f.close()
finally:
    print("Cleanup done")


# ---------- 9. CSV FILES (Comma-Separated Values) ----------

# Definition: CSV is a simple file format for tabular data where each line is a row and commas separate columns.

import csv

# Read CSV as lists of strings
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # row is a list like ["Name", "Age"]

# Read CSV as dictionaries (first row becomes keys)
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])   # Access by column name

# Write CSV (list of rows) - newline='' prevents blank lines on Windows
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])   # Write header
    writer.writerow(["Alice", 30])     # Write data row

# Write CSV with dictionaries
with open("output.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()               # Writes column names
    writer.writerow({"Name": "Bob", "Age": 25})

# Custom delimiter and quoting
with open("data.tsv", "w", newline="") as f:
    writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_ALL)
    writer.writerow(["Hello, world", "value"])

# Using csv.register_dialect() for reusable formats
csv.register_dialect('myformat', delimiter='|', quoting=csv.QUOTE_MINIMAL)
with open("data.txt", "r") as f:
    reader = csv.reader(f, dialect='myformat')


# ---------- 10. JSON FILES (JavaScript Object Notation) ----------

# Definition: JSON is a text format for storing structured data that looks very similar to Python dictionaries and lists.

import json

# Write Python object to JSON file
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)   # indent=2 makes it human-readable

# Read JSON file back into Python object
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])          # Accesses like a dictionary

# Convert between string and object (no file involved)
json_string = json.dumps(data)     # Python dict → JSON string
obj = json.loads(json_string)      # JSON string → Python dict

# Handle non-serializable objects (e.g., datetime)
from datetime import datetime
data_with_date = {"now": datetime.now()}
json_str = json.dumps(data_with_date, default=str)  # converts datetime to ISO string

# Custom JSON decoder/encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
json_str = json.dumps(data_with_date, cls=CustomEncoder)


# ---------- 11. PICKLE (Object Serialization) ----------

# Definition: Pickle converts any Python object to bytes and back.
# ⚠️ WARNING: Pickle is insecure. Only unpickle data you trust.

import pickle

data = {"name": "Alice", "scores": [100, 90]}

# Write pickle
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Read pickle
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

# Pickle protocol versions: 0-5 (higher is more efficient but not backward compatible)
pickle.dump(data, open("data.pkl", "wb"), protocol=pickle.HIGHEST_PROTOCOL)


# ---------- 12. IN-MEMORY FILES (StringIO, BytesIO) ----------

# Definition: File-like objects that live in RAM, not on disk.

from io import StringIO, BytesIO

# For text
text_io = StringIO()
text_io.write("Hello")
text_io.getvalue()      # "Hello"
text_io.seek(0)
text_io.read()          # "Hello"

# For binary
bytes_io = BytesIO()
bytes_io.write(b"abc")
bytes_io.getvalue()     # b'abc'

# Use with csv.writer
output = StringIO()
writer = csv.writer(output)
writer.writerow(["a", "b"])
csv_data = output.getvalue()


# ---------- 13. WORKING WITH ARCHIVES (zipfile, tarfile) ----------

# Definition: Read and write ZIP and TAR archives.

import zipfile

# Create a ZIP file
with zipfile.ZipFile("archive.zip", "w") as zf:
    zf.write("file1.txt")
    zf.write("file2.txt")

# Extract all files
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extractall("extracted_folder")

# Read a specific file from ZIP
with zipfile.ZipFile("archive.zip", "r") as zf:
    with zf.open("file1.txt") as f:
        content = f.read().decode()

# Tarfile (similar)
import tarfile
with tarfile.open("archive.tar.gz", "w:gz") as tf:
    tf.add("file1.txt")
with tarfile.open("archive.tar.gz", "r:gz") as tf:
    tf.extractall("extracted_folder")


# ---------- 14. TEMPORARY FILES AND DIRECTORIES ----------

import tempfile

# Temporary file (auto-deleted when closed)
with tempfile.TemporaryFile(mode="w+") as tf:
    tf.write("temp data")
    tf.seek(0)
    print(tf.read())   # "temp data"

# Named temporary file (visible in filesystem)
with tempfile.NamedTemporaryFile(mode="w", delete=False) as tf:
    tf.write("data")
    path = tf.name
# Later: os.remove(path)

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    path = Path(tmpdir) / "file.txt"
    path.write_text("content")
# Directory automatically deleted


# ---------- 15. READING LARGE FILES IN CHUNKS ----------

# Definition: For huge files, read in fixed-size chunks to avoid memory overflow.

def read_in_chunks(file_path, chunk_size=8192):
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
for chunk in read_in_chunks("large_file.bin"):
    process(chunk)   # e.g., write to another file


# ---------- 16. FILE PERMISSIONS AND METADATA ----------

# Definition: Get and set file permissions (Unix-like systems).

import stat

# Get permissions
mode = os.stat("file.txt").st_mode
oct(mode & 0o777)      # e.g., '0o644'

# Set permissions (read-write for owner, read-only for others)
os.chmod("file.txt", 0o644)

# Check if it's a file or directory
os.path.isfile("file.txt")
os.path.isdir("folder")

# Get modification time
mtime = os.path.getmtime("file.txt")   # Unix timestamp
from datetime import datetime
print(datetime.fromtimestamp(mtime))


# ---------- 17. QUICK REFERENCE ----------

# | Task                          | Code                                      |
# |-------------------------------|-------------------------------------------|
# | Read entire file              | `with open(f) as f: content = f.read()`  |
# | Read lines into list          | `lines = f.readlines()`                  |
# | Iterate over lines            | `for line in f:`                         |
# | Write a string                | `f.write("text")`                        |
# | Write multiple lines          | `f.writelines(list)`                     |
# | Append to file                | `open(f, "a")`                           |
# | Check if file exists          | `os.path.exists(path)`                   |
# | Delete a file                 | `os.remove(path)`                        |
# | Rename a file                 | `os.rename(old, new)`                    |
# | Copy a file                   | read from one, write to another          |
# | Read CSV as lists             | `csv.reader(f)`                          |
# | Read CSV as dicts             | `csv.DictReader(f)`                      |
# | Write CSV                     | `csv.writer(f).writerow(row)`            |
# | Read JSON                     | `json.load(f)`                           |
# | Write JSON                    | `json.dump(data, f)`                     |
# | Seek to position              | `f.seek(10)`                             |
# | Get current position          | `f.tell()`                               |
# | Walk directories              | `os.walk(root)`                          |
# | Find files by pattern         | `glob.glob("*.py")`                      |
# | Copy file with shutil         | `shutil.copy(src, dst)`                  |
# | Delete folder tree            | `shutil.rmtree(path)`                    |
# | CSV with delimiter            | `csv.reader(f, delimiter='\t')`          |
# | CSV with quoting              | `csv.writer(f, quoting=csv.QUOTE_ALL)`   |
# | Pickle dump/load              | `pickle.dump(obj, f)`, `pickle.load(f)`  |
# | StringIO (in‑memory text)     | `s = StringIO(); s.write("text")`        |
# | BytesIO (in‑memory binary)    | `b = BytesIO(); b.write(b'data')`        |
# | Multiple `with` files         | `with open(a) as a, open(b) as b:`       |
# | Read large file in chunks     | `while chunk := f.read(8192): process(chunk)` |
# | Create ZIP archive            | `with zipfile.ZipFile("a.zip","w") as zf: zf.write(f)` |
# | Temporary file                | `with tempfile.TemporaryFile() as tf:`   |