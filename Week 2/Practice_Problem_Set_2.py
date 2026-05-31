# --- Problem Set 2 ---

"""
# camel.py
def main():
    camel_case = get_camel_case()
    snake_case = get_snake_case(camel_case)
    print(f"snake_case: {snake_case}")

def get_camel_case():
    camel_case = input("camelCase: ")
    return camel_case

def get_snake_case(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()

    

# coke.py
def main():
    due = 50
    while due > 0:
        print(f"Amount due: {due}")
        coin = int(input("Insert coin: "))
        if coin in (25, 10, 5): 
            due -= coin
        else:
            continue
    if due < 0: 
        print(f"Change owed: {abs(due)}")

if __name__ == "__main__":
    main()


    
# twttr.py
def main():
    text = get_input()
    output = get_output(text)
    print(f"Output: {output}")

def get_input():
    text = input("Input: ")
    return text

def get_output(text):
    output = ""
    for char in text:
        if char.lower() in ("a", "e", "i", "o", "u"):
            continue
        else: 
            output += char
    return output

if __name__ == "__main__":
    main()

    

# plates.py 
def main():
    plate = get_plate()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def get_plate():
    plate = input("Plate: ")
    return plate

def is_valid(plate):
    # Length check
    if not 2 <= len(plate) <= 6:
        return False
    
    # First two letters
    for char in plate[0:2]:
            if not char.isalpha():
                return False
    # All characters alphanumeric
    if not plate.isalnum():
        return False
    
    # Number rules
    found_number = False
    for i in plate:
        if i.isdigit():
            found_number = True
            if i == "0":
                return False
        elif found_number and i.isalpha():
            return False
    
    return True

    
    
# nutrition.py
def main():

    fruits_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80 }

    item = get_item()
    cals = get_cals(item, fruits_calories)
    if cals:
        print(f"Calories: {cals}")

def get_item():
    item = input("Item: ").lower()
    return item
    
def get_cals(item, fruits_calories):
    cals = fruits_calories.get(item, "")
    return cals

if __name__ == "__main__":
    main()
"""