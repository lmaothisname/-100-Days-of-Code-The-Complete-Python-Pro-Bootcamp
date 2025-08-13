# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

placeholder =  ""
for replace in range(1,len(chosen_word) + 1):
    placeholder += "-"
print(placeholder)
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""
for letter in chosen_word:
    if guess == letter:
        display += letter
    else:
        display += "-"
print(display)