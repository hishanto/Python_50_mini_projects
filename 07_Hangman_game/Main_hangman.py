import random
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list) #select word
wordlen = len(chosen_word)  # length of the word

print(chosen_word)
placeholder = []
for space in range(wordlen):
    placeholder.append("_")
placeholderStr = ''.join(placeholder)
print(placeholderStr)   #print out the placeholder
# loop for guess till game is finished
while "_" in placeholder:
    guess = input("Guess a letter:  ").lower() # lower case the guess to avoid complication
    index = 0
    for letter in chosen_word:

        if letter == guess:
            placeholder[index] = guess
        index += 1

    placeholderStr = ''.join(placeholder)
    print(placeholderStr)