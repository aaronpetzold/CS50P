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
        "December",
    ]

    m, d, y = get_date(months)
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

        else:
            continue


def date_check(m, d, y):
    if 1 <= m <= 12 and 1 <= d <= 31 and y > 0:
        return True


if __name__ == "__main__":
    main()
