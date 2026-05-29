menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0
total = 0

while True:
    try: 
        item = input("Item: ").title()
        price = menu.get(item)
        total += price
    except (ValueError, KeyError, TypeError):
        continue
    except EOFError:
        break
    else:
        print(f"Total: ${total:.2f}")
        

