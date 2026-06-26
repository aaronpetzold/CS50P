i = 0

while i < 50:
    print(f"Amount due: {50 - i}")
    money = int(input("Insert Coin: "))

    if money == 25 or money == 10 or money == 5:
        i += money

if i > 50:
    change = i - 50
    print(f"Change owed: {change}")
else:
    print("Change owed: 0")
