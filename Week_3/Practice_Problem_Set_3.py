# --- Problem Set 3 ---

"""
# fuel.py
def main():
    x, y = get_fraction()
    output = get_output(x, y)
    print(output)

def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if not (x > y or y <= 0 or x < 0):
                return x, y
        except ValueError:
            continue

def get_output(x, y):
    output = round(x / y * 100)
    if output >= 99:
        return "F"
    elif output <= 1:
        return "E"
    else:
        return f"{output}%"

if __name__ == "__main__":
    main()



# taqueria.py
def main():
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

    total = 0
    while True:
        try: 
            item = input("Item: ").title()
            price = menu.get(item, "")
            if price != "":
                total += price
                print(f"Total: ${total:.2f}")
            else:
                continue
        except EOFError: 
            break

if __name__ == "__main__":
    main()

    

# grocery.py
def main():
    grocery_list = {}
    while True: 
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                grocery_list[item] = 1
        except EOFError: 
            print()
            break
    
    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item}")

if __name__ == "__main__":
    main()

    

# outdated.py
def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    m, d ,y = get_date(months)
    print(f"{y}-{m:02}-{d:02}")

def get_date(months):
    while True:
        
        date = input("Date: ")
        if "/" in date:
            try: 
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)
                y = int(y)
                if date_check(m, d, y):
                    return m, d, y
                else: 
                    continue
            except:
                continue

        elif "," in date:
            try:
                date = date.replace(",", "")
                m, d, y = date.split(" ")
                if m in months:
                    m = months.index(m) + 1
                    d = int(d)
                    y = int(y)
                    if date_check(m, d, y):
                        return m, d, y
                else: 
                    continue
            except:
                continue

        else: continue

def date_check(m, d, y):
    if 1 <= m <= 12 and 1 <= d <= 31 and y > 0:
        return True


if __name__ == "__main__":
    main()
"""