# === Loops ===

# While loop
i = 0
while i < 5:
    print(i)
    i += 1  # Don't forget this!

# While with break
while True:
    n = input("Enter number (or 'quit'): ")
    if n == "quit":
        break  # Exit loop
    print(f"You entered: {n}")

# While with continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# For loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):       # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step 2)
    print(i)

# For with strings/list
for char in "Hello":
    print(char)  # H, e, l, l, o