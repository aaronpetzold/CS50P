# --- Problem Set 0 ----

"""
# indoor.py
text = input().lower()
print(text)



# playback.py
replaced = input().replace(" ", "...")
print(replaced)



# faces.py
def main():
    text = input()
    converted = convert(text)
    print(converted)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

if __name__ == "__main__":
    main()



# einstein.py
def main():
    c = 300000000
    m = get_mass()
    print(f"E: {m * c * c}")

def get_mass():
    mass = int(input("m: "))
    return mass

if __name__ == "__main__":
    main()

    
    
# tip.py
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = float(d.strip("$"))
    return d

def percent_to_float(p):
    p = float(p.strip("%"))/100
    return p

if __name__ == "__main__":
    main()
"""