import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False
    for part in ip.split("."):
        if not (0 <= int(part) <= 255):
            return False
        if len(part) > 1 and part[0] == "0":
            return False
    return True


if __name__ == "__main__":
    main()
