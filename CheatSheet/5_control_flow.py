# === Control Flow ===

# If/Elif/Else
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# One-line if
status = "Adult" if age >= 18 else "Minor"

# Nested if 
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need license")
else:
    print("Too young")

# Boolean operators
if age >= 13 and age <= 19:
    print("Teenager")
    
if score > 90 or extra_credit:
    print("Grade: A")

# Match/Case (Python 3.10+)
command = input("Command: ")

match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":  # Multiple values
        print("Stopping...")
    case "help":
        print("Help menu")
    case _:  # Default
        print("Unknown command")