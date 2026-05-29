def main():
    x = get_int("What´s x: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:    
            return int(input(prompt))
        except ValueError:
            pass
        
'''
    while True:
        try:    
            x = int(input("What´s x: "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
        # or
        # else:
        #   return x
'''

main()




