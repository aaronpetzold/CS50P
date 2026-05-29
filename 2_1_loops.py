''''
while True:
    i = int(input("How often): "))
    if i < 100:
        while i != 0:
         print("meow")
         i = i - 1
    else:
        print("Smaller!")     


i = 0
x = int(input("How often): "))
while i < x:
    print("moew")
    i = i + 1 
    # or just i += 1


x = int(input("How often?: "))
for _ in range(x):
    print("meow")

    
x = int(input("How often?: "))
print("meow\n" * x, end="")


while True: 
    n = int(input("n: "))
    if n > 0:
        break
for _ in range(n):
    print("meow")    

    
def main():
    number = get_number()
    meow(number)
def get_number():
    while True:
        n = int(input("n:"))
        if n > 0:
            return n    
def meow(n):
    for _ in range(n):
        print("meow")
main()        


students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


students = {"Hermione": "Gryffindor",
            "Harry" : "Gryffindor",
            "Ron" : "Gryffindor",
            "Draco" : "Slytherin"}

for student in students:
    print(student, students[student], sep=", ")   


students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Rack Russell terrier"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"])    
'''


