"""
name = input("What´s your name?: ").strip().title()
first, last = name.split(" ")
print(f"hello, {name}")


x = float(input("What´s x: "))
y = float(input("What´s y: "))
z = round(x + y)
z = round(x / y, 2)
print(f"{x} / {y} = {z:,}")
print(f"{x} / {y} = {z:.2f}")


def main():
    name = input("What´s your name: ")
    hello(name)

def hello(to="world"):
    print(f"hello {to}")

main()


def main():
    x = int(input("What´s x: "))
    print("x square is", square(x))

def square(n):
    return pow(n, 2)

main()
"""







