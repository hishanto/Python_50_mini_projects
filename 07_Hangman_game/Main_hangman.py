word_list = ["aardvark", "baboon", "camel"]

import random
import Hangman_asciiArt

print(Hangman_asciiArt.logo)
word_list = ["aardvark", "baboon", "camel"]
lives = 6 # number of choices a player will have

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
display = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")
display = "".join(placeholder)
print(display)
game_over = False
while not game_over and lives > 0 :
    guess = input("Guess a letter: ").lower()


    if guess in chosen_word:
        for index,letter in enumerate(chosen_word) :
            if letter == guess:
                placeholder[index] = letter
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        print(Hangman_asciiArt.stages[lives])

    display = "".join(placeholder)
    print(display)

    if "_" not in display:
        game_over = True
        print("You win")
if lives == 0 and "_" in placeholder:
    print("You lose! The word was:", chosen_word)