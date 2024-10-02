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
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(hangman_words)
    hint = ["_"] * len(answer)
    print(hint)

if __name__ == "__main__":
    main()