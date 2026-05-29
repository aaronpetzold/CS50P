months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def check(date):
    if "/" in date:
        try: 
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            return month, day, year 
        except ValueError:
            return None

    elif "," in date:
        try:
            month, rest = date.split(" ")
            day, year = rest.split(", ")
            month = months[month]
            day = day.replace(",", "")
            month = int(month)
            day = int(day)
            year = int(year)
            return month, day, year 
        except (ValueError, KeyError):
            return None
    
    else:
        return None

def range(month, day, year): 
    if month in range(1, 13) and day in range(1, 32) and year >= 0:
        return True
    else:
        return False
    
def main(): 
    while True:
        date = input("Date: ")
        result = check(date)

        if result == None:
            continue

        month, day, year = result
        if not range(month, day, year):
            continue

        print(f"{year}-{month:02d}-{day:02d}")


main()



        
