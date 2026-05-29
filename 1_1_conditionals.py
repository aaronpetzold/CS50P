'''
x = int(input("What´s x: "))
y = int(input("What´s y: "))

if x < y:
    print("x is less than y")
elif x > y:
 print("x is greater than y")
else:
    print("x is equal to y")

    
while True:
    score = int(input("Score: "))
    if 0 <= score <= 100:
        break
    print("Invalid score!")

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("c")
elif score >= 60:
    print("D")
else:
    print("F")      


def main():
    x = int(input("What´s x: "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False 
    #return True if n % 2 == 0 else False
    # or
    #return n % 2 == 0
    
main()  


name = input("What´s your name: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
'''
