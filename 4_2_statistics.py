'''
import statistics


mean = statistics.mean([100, 90])
print(mean)
'''

import statistics

numbers = []

while True:
    try: 
        numbers.append(int(input("Enter a number: ")))

        while True: 
            repeat = input("Do you want to add another number? (Y/N): ").lower()
            if repeat in ["y", "n"]:
                break
            else:
                print("Please enter 'Y' or 'N'!")

        if repeat == "n":
            break
        
    except ValueError:
        print("Please enter a valid number!")

mean = statistics.mean(numbers)
print(mean)
