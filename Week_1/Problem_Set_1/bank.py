greeting = input("Greeting: ")

greeting = greeting.strip().lower()

if greeting[:5] == "hello":
    cash = 0
elif greeting.startswith("h"):
    cash = 20
else:
    cash = 100

print(f"${cash}")
