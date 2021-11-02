import random
from hangman_words import word_list
from hangman_art import stages, logo
from os import system

lives = 6
end_of_game = False

word = random.choice(word_list)
word_length = len(word)

print(logo)

# Testing code
print(f"the solution is {word}")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    system('clear')

    if guess in word:
        print(f"You've already guessed {guess}")

    for i in range(word_length):
        letter = word[i]
        if guess == letter:
            display[i] = letter

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You Won!")

    if lives == 0:
        end_of_game = True
        print("You Lose!")

    print(stages[lives])