import random

cards = ["jack", "queen", "king"]


def main():
    # print(random.choices(cards, k=2))
    # print(random.sample(cards, k=2))
    # print(random.choices(cards, weights = [100, 0, 0], k=2))
    random.seed(0)
    print(random.choices(cards, k=2))


main()
