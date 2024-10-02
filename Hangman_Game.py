# Hangman_Game

#this_section_handles_the_greetings

def greet_the_players():
    print("Howdy Players!")
    print("....")
    print("Welcome to Hangman!")
    print("....")
    print("Your word category for today is...")
    print("....")
    print("fruits!")
    print("....")
    print("You may start, Good luck!")

import random

hangman_words = ("apple", "banana", "lychee", "grapes", "orange", "pineapple", "coconut", "watermelon", "lemon", "kiwi")

#dictionary of key():
hangman_art ={0: ("     ",
                  "     ",
                  "     "),
              1: ("  o  ",
                  "     ",
                  "     "),
              2: ("  o  ",
                  "  |  ",
                  "     "),
              3: ("  o  ",
                  " /|  ",
                  "     "),
              4: ("  o  ",
                  " /|\\",
                  "     "),
              5: ("  o  ",
                  " /|\\",
                  " /   "),
              6: ("  o  ",
                  " /|\\",
                  " / \\")}

def display_man(wrong_guesses):
    print("**|****")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*******")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(hangman_words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    greet_the_players()

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

if __name__ == "__main__":
    main()