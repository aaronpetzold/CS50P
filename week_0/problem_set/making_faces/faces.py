def convert(input):
    input = input.replace(":)", "🙂")
    input = input.replace(":(", "🙁")
    return input


def main():
    message = input("What do you have to say? (Use emojis!!!): ")
    converted = convert(message)
    print(converted)


main()
