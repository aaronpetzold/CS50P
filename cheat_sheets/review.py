"""
# --- Variables ---
name = "Bob"
print("Hello, " + name + "!")

# --- Data types ---
text = "apple"
number = 10
decimal = -10.123
has_money = False 

#Tuple - list-like structure, can´t be changed after creation (immutable)
coordinates = (2.5, 1.5, 1.0)

#List - mutable
names = ["Agnetha", "Björn", "Benny", "Anni-Frid"]

#Set - no duplicates
unique = {1, 2, 3, 4, 5}

#Dictionary - holds key-value pairs
users = {"Bob" : 1, "James" : 2}

#Conversion
number = "100"
number = int(number)
print(10 + number)
# OR print(10 + int(number))

# --- Type annotations ---
age: int = 10
name: str = "Bob"

# --- F-strings ---
print(f"Name: {name}, Age: {age}")
# f means format

# --- Functions ---
def add(a: float, b: float) -> float: 
    print(f"Adding {a} + {b}")
    return a + b
print(add(a=10, b=15))
print(add(a=30, b=45))

def greet(name: str, greeting: str) -> None:
    print(f"{greeting}, {name}!")
greet(name= "Bob", greeting= "Ciao")

def greet(name: str, greeting: str = "Hi") -> None:
        print(f"{greeting}, {name}!")
greet("Bob")

#no parameters needed!
def func() -> None:
     print("Hello")
func()

# --- Looping ---

# --- For-loop ---
#-often used with lists
#-finite
for i in range(3):
    print("Hello")

for name in names:
    print(f"Hello, {name}")

# --- While-loop ---
#-infinite
#-conditions used
while True:
    print("Hello")

i: int = 0
while i < 3:
    print(i)
    i += 1

# --- Comparision operators ---
a: int = 1
b: int = 2

print(a > b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# --- if, elif, else ---
while True:
    user_input: str = input("You: ")

    if user_input == "hello":
        print("Bot: Hello!")
    elif user_input == "how are you":
        print("Bot: Good, how about you?")
    else:
        print("Bot: Sorry i did not understand that.")

# --- Error handling ---
try:
    a, b = 10, "fifteen"
    print(a + b)
except TypeError as e:
    print(f"Please enter a number in the form of an integer or a float!")
except Exception as e:
    #Exception is bad practice, only use as last resort
    print("Something else went wrong...")

print("Continuing with the program...")

# --- Imports ---
import math
import math as m
from math import sqrt, tan

print(math.sqrt(3))
print(m.sqrt(4))
print(sqrt(5))
print(tan(2))
"""
# --- Creating your first project ---
bot_name: str = "Bob"
print(f"Hello I\"m {bot_name}! How can I assist you today?")

while True: 
    user_input: str = input("You: ").lower()

    if user_input in ["hi", "hello"]: 
        print(f"{bot_name}: Hi there! How can i help you?")
    elif user_input in ["bye", "see you"]:
        print(f"{bot_name}: Goodbye! Have a great day!")
    elif user_input in ["+", "add"]:
        print(f"{bot_name}: Sure! Let's do some addition! Please enter twp numbers.")
        try:
            num1: float = float(input("First number: "))
            num2: float = float(input("Second number: "))
            print(f"{bot_name}: The sum is {num1 + num2}")
        except ValueError:
           print(f"{bot_name}: Oops! That doesn't seem like a valid number. Try again!")
    else:
        print(f"{bot_name}: I'm sorry, I don#t understand that. Please try again.")