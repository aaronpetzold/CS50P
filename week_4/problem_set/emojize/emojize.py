from emoji import emojize


def main():
    code = get_code()
    output = get_output(code)
    print(f"Output: {output}")


def get_code():
    code = input("Input: ")
    return code


def get_output(code):
    output = emojize(code, language="alias")
    return output


if __name__ == "__main__":
    main()
