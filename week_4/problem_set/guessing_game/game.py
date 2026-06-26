from random import randint


def main():
    level = get_level()
    random_number = generate_random(level)
    guessing(random_number)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            continue
    return level


def generate_random(level):
    random_number = randint(1, level)
    return random_number


def guessing(random_number):
    while True:
        try:
            while True:
                guess = int(input("Guess: "))
                if guess > 0:
                    break

            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too small!")
            else:
                print("Just right!")
                return
        except ValueError:
            continue


if __name__ == "__main__":
    main()
