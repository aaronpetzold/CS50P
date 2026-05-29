# === Input/Output ===

# Basic input
name = input("What's your name? ")          # String input
age = int(input("How old are you? "))       # Convert to int
height = float(input("Height in meters: ")) # Convert to float

# Multiple inputs on one line
x, y = input("Enter two numbers: ").split()
x, y = int(x), int(y)

# With validation
while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid! Enter a number.")