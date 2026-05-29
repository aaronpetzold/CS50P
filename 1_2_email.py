
while True: 
    name = input("Name: ").strip().title()
    email = input("E-Mail: ").lower()

    if "@" in email: 
        print(f"Hallo {name}! Deine E-Mail ist {email}")
    else:
        print("Ungültige E-Mail!")
    
    repeat = input("Möchten sie wiederholen? (J/N): ").title()
    if repeat != "J":
        break
       
