'''
WORDS = {"PAIR" : 4, "HAIR" : 4, "CHAIR" : 5, "GRAPHIC" : 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You´ve won")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job you scored {points} points.")
main()
'''

WORDS = {"PAIR" : 4, "HAIR" : 4, "CHAIR" : 5, "GRAPHIC" : 7}

def main():
    print("Welcome to Spelling Bee!")
    for word, points in WORDS.items():
        print(f"{word} was worth {points}.")

   

main()