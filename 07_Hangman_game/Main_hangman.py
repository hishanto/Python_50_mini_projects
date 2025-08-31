word_list = ["aardvark", "baboon", "camel"]

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
display = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")
display = "".join(placeholder)
print(display)
while "_" in placeholder:
    guess = input("Guess a letter: ").lower()

    index = 0


    for letter in chosen_word:
        if letter == guess:
            placeholder[index] = letter
        index += 1
    display = "".join(placeholder)
    print(display)