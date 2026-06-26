def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    chapter1 = contents[11:246]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)


if __name__ == "__main__":
    main()
