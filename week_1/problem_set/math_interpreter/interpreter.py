input = input("Expression: ").strip()

x, y, z = input.split()

x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        if z != 0:
            print(x / z)
        else:
            print("You can´t divide by 0!")
    case _:
        print("Invalid operator!")
