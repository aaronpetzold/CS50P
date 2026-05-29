# === Functions ===

# Basic function
def greet(name):
    print(f"Hello {name}!")

greet("Alice")  # Call function

# Function with return
def square(x):
    return x * x

result = square(5)  # result = 25

# Multiple returns
def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([1, 5, 3, 9])

# Default parameters
def greet(name="World"):
    print(f"Hello {name}!")

greet()          # Hello World!
greet("Alice")   # Hello Alice!

# Type hints (optional)
def add(x: int, y: int) -> int:
    return x + y

# Main function pattern
def main():
    # Your main code here
    print("Program running")

if __name__ == "__main__":
    main()  # Only runs if file is executed directly