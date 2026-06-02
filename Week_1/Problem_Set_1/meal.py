def main():
    time_str = input("What time is it? ")
    time = convert(time_str)
    output = get_output(time)
    if output:
        print(output)


def convert(time_str):
    hour, minute = time_str.split(":")
    return float(hour) + float(minute) / 60


def get_output(time):
    if 7.0 <= time <= 8.0:
        return "breakfast time"
    elif 12.0 <= time <= 13.0:
        return "lunch time"
    elif 18.0 <= time <= 19.0:
        return "dinner time"
    else:
        return ""


if __name__ == "__main__":
    main()
