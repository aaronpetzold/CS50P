# === CSV File Handling (CS50P Lesson) ===

# ---------- READING: BASIC SPLIT ----------
# Definition: rstrip() removes the newline character at the end of each line.
# split(",") separates the line into a list wherever a comma appears.
# This creates a list where index 0 is the name and index 1 is the house.

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


# ---------- READING: UNPACKING ----------
# Definition: Unpacking assigns each element of the list to a separate variable.
# This is cleaner than using indexes because variable names are more meaningful.

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


# ---------- READING: STORING IN DICTIONARIES ----------
# Definition: Dictionaries store related data together with named keys.
# Storing data in a list of dictionaries allows sorting and filtering later.

students = []
with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        students.append({"name": name, "home": home})

# Definition: sorted() returns a new sorted list. The key parameter tells Python
# what value to sort by. lambda student: student["name"] means "use the name field".
for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is in {student['home']}")


# ---------- READING: CSV.READER ----------
# Definition: csv.reader is a module that properly handles CSV formatting.
# It works even when values contain commas (by using quotes) or newlines.
# It returns each row as a list of strings.

import csv

students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


# ---------- READING: CSV.DICTREADER ----------
# Definition: csv.DictReader uses the first row of the CSV file as column headers.
# Each row is returned as a dictionary where keys are the header names.
# This is the most readable approach when your CSV has headers.

import csv

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


# ---------- WRITING: CSV.WRITER ----------
# Definition: csv.writer converts a list into a properly formatted CSV row.
# It handles quoting automatically if values contain commas.
# "a" mode opens the file for appending (adds to end without deleting existing data).

import csv

name = input("What's your name? ")
home = input("Where's your house? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


# ---------- WRITING: CSV.DICTWRITER ----------
# Definition: csv.DictWriter writes dictionaries as CSV rows.
# The fieldnames parameter defines the order of columns in the output file.

import csv

name = input("What's your name? ")
home = input("Where's your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})