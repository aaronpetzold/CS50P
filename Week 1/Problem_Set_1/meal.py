
def main():
    time = input("What time is it? ")
    
    hours, minutes = convert(time)

    if (hours == 8 and minutes == 0) or hours == 7:
        print("breakfast time")
    elif (hours == 13 and minutes == 0) or hours == 12:
        print("lunch time")
    elif (hours == 19 and minutes == 0) or hours == 18:
        print("dinner time")
    else:
        print()

def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)
    return hours, minutes

main()
    