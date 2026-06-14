# === Loops ===


# ========== TABLE OF CONTENTS ==========
#
# 1. WHILE LOOP
# 2. BREAK AND CONTINUE
# 3. FOR LOOP WITH range()
# 4. LOOPING OVER SEQUENCES (list, str, tuple)
# 5. ENUMERATE (index and value)
# 6. ZIP (parallel iteration)
# 7. FOR...ELSE (else after loop)
# 8. NESTED LOOPS
# 9. LOOP OPTIMIZATION TIPS
#
# ========================================


# Definition: Loops repeat a block of code multiple times.
# Python has two loop constructs: `while` and `for`.


# ---------- 1. WHILE LOOP ----------

# Repeats as long as the condition is True.
i = 0
while i < 5:
    print(i)
    i += 1          # Don't forget to update the counter!


# ---------- 2. BREAK AND CONTINUE ----------

# break: exits the loop immediately.
while True:
    n = input("Enter number (or 'quit'): ")
    if n == "quit":
        break       # Exit loop
    print(f"You entered: {n}")

# continue: skips the rest of the current iteration, goes to next.
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue    # Skip even numbers
    print(i)


# ---------- 3. FOR LOOP WITH range() ----------

# range(stop) → 0, 1, 2, ..., stop-1
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

# range(start, stop) → start, start+1, ..., stop-1
for i in range(2, 6):       # 2, 3, 4, 5
    print(i)

# range(start, stop, step) → start, start+step, ...
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# Count downward
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
    print(i)


# ---------- 4. LOOPING OVER SEQUENCES (list, str, tuple) ----------

# Over a string – iterates characters.
for char in "Hello":
    print(char)   # H, e, l, l, o

# Over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Over a tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)


# ---------- 5. ENUMERATE (index and value) ----------

# Get both index and element in a loop.
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")   # 0: apple, 1: banana, ...

# Start index at 1 instead of 0.
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")   # 1: apple, 2: banana, ...


# ---------- 6. ZIP (parallel iteration) ----------

# Iterate over multiple sequences simultaneously (stops at shortest).
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip with three or more lists.
ages = [30, 25, 35]
for name, score, age in zip(names, scores, ages):
    print(f"{name} (age {age}) scored {score}")


# ---------- 7. FOR...ELSE (else after loop) ----------

# The else block runs if the loop completes normally (no break).
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

# The else does NOT run if the loop is terminated by break.
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not run because of break.")


# ---------- 8. NESTED LOOPS ----------

# Loop inside a loop.
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# ---------- 9. LOOP OPTIMIZATION TIPS ----------

# Use local variables for speed (especially in large loops).
# Avoid repeated attribute lookups inside the loop.
# Prefer list comprehensions for simple transformations.
# Use `while` when you don't know the number of iterations in advance.