from datetime import date
import sys
import inflect


def main():
    birth_date = get_birth_date()
    todays_date = get_todays_date()
    days = get_days(birth_date, todays_date)
    minutes = get_minutes(days)
    minutes_in_words = get_minutes_in_words(minutes)
    print(minutes_in_words)


def get_birth_date():
    date_input = input("Date of Birth: ")
    try:
        return parse_date(date_input)
    except ValueError:
        sys.exit("Invalid date")


def parse_date(date_str):
    year, month, day = date_str.split("-")
    return date(int(year), int(month), int(day))


def get_todays_date():
    return date.today()


def get_days(birth, today):
    delta = today - birth
    if delta.days < 0:
        sys.exit("Invalid date")
    return delta.days


def get_minutes(days):
    return days * 24 * 60


def get_minutes_in_words(m):
    p = inflect.engine()
    return p.number_to_words(m).replace(" and ", " ").capitalize() + " minutes"


if __name__ == "__main__":
    main()
