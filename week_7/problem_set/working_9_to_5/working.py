import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start_raw, end_raw = s.split(" to ")
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM)$"
    start_match = re.search(pattern, start_raw.strip())
    end_match = re.search(pattern, end_raw.strip())

    if not start_match or not end_match:
        raise ValueError

    start_hour = int(start_match.group(1))
    start_min = int(start_match.group(2)) if start_match.group(2) else 0
    start_period = start_match.group(3)

    end_hour = int(end_match.group(1))
    end_min = int(end_match.group(2)) if end_match.group(2) else 0
    end_period = end_match.group(3)

    start_hour, start_min = to_24hour(start_hour, start_min, start_period)
    end_hour, end_min = to_24hour(end_hour, end_min, end_period)

    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


def to_24hour(hour, minute, period):
    if not (1 <= hour <= 12 and 0 <= minute <= 59):
        raise ValueError

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return hour, minute


if __name__ == "__main__":
    main()
