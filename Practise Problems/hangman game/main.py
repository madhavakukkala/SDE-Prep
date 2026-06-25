import random
from wordslist import words

hangman_art = {
    0: (
        "   ",
        "   ",
        "   "
    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}

def show_man(wrong_guesses):
    print("******************************")

    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************************")


def show_hint(hint):
    print(" ".join(hint))

def show_answer(answer):
    print(" ".join(answer))



def main():

    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        show_man(wrong_guesses)
        show_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        elif hint == answer:
            
            print("You win!")
            is_running = False

        else:
            wrong_guesses += 1

        if "_" not in hint:
            show_man(wrong_guesses)
            show_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            show_man(wrong_guesses)
            show_answer(answer)
            print("YOU LOSE!")
            is_running = False







if __name__ == '__main__':
    main()
