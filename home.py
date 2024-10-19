from logo import hangman_stages, Hangman_logo
from ascii_art import ascii
print(Hangman_logo)
import os
def clear():
    os.system('cls')
word_list = ["Sebastian pato"]
import random
secret_word = random.choice(word_list)
lenght_word = len(secret_word)
blanks = []
for _ in range(lenght_word):
    blanks.append("_")
print(blanks)
guessed_letters = []
lives = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ")
    guess = guess.upper()


    if guess in guessed_letters:
        print("You've already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)
    for position in range(lenght_word):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose!")
    print(" ".join(blanks))
    print(hangman_stages[lives])
    if "_" not in blanks:
        end_game = True
        print("You win!" and print(ascii))
    if end_game:
        ask = input("Do you want to play again? (Y/N)")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            lenght_word = len(secret_word)
            for _ in range(lenght_word):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time")

