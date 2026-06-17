import random
import time

#List of words
words = ["python", "computer", "football", "keyboard", "internet", "momos", "india", "delhi"]

#Random world selection
secret_word = random.choice(words)

#Empty list to store gussed letters
guessed_letters = []

#Total chances
chances = 6

print("=========================")
print("WELCOME TO HANGMAN GAME")
print("=========================")

name = input("Enter your name:")
print(f"\nHello{name}! Let's start the game...")
time.sleep(1)

while chances > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"

    print("\nWord :", display_word)

     #Check if player won
    if "_" not in display_word:
         print("\n Congratulations! you guessed the word.")
         break
        #User input
    guess = input("Guess a letter:").lower()

        #validation
    if len(guess)!= 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue
        #Already guessed
    if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
    guessed_letters.append(guess)

        #correct guess
    if guess in secret_word:
            print("Correct Guess!")
    else:
        chances -= 1
        print("Wrong Guess!")
        print("Reamaining Chances:", chances)

#If player loss
if chances == 0:
    print("\n Game Over!")
    print("Correct word was:", secret_word)
print("\n Thanks for playing")   
