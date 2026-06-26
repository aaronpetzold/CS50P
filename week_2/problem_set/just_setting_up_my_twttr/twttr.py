text = input("Enter something: ")
result = ""

for c in text:
    if not c.lower() in "aeiou":
        result += c

print(f"Result: {result}")
