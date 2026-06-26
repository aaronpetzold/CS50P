def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    count = 0
    counter = 0
    valid = True

    for c in plate:
        count += 1
    if not (count >= 2 and count <= 6):
        valid = False

    if not plate.isalnum():
        valid = False

    for c in plate[0:2]:
        if not c.isalpha():
            valid = False

    for c in plate:
        counter += 1
        if c.isdigit():
            break

    if c != "0":
        for i in plate[counter:]:
            if not i.isdigit():
                valid = False
                break
    else:
        valid = False
    return valid


if __name__ == "__main__":
    main()
