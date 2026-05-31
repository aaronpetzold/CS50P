
while True:
    fraction = input("Fraction: ")

    try:
        x, y = fraction.split("/")
        x = float(x)
        y = float(y)
        result = x / y
        if x > 0 and y > 0 and x <= y:
            break
    except (ValueError, ZeroDivisionError):
        continue

result = round(result * 100)

if result >= 99:
    print("F")
elif result <= 1:
    print("E")
else:
    print(f"{result}%")

