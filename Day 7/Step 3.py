import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
# TODO-1: - Use a while loop to let the user guess again.
check = False
word = []
while check != True:
    guess = input("Guess a letter: ").lower()
    display = ""
# TODO-2: Change the for loop so that you keep the previous correct letters in display.
    store = display
    for letter in chosen_word:
        if letter == guess:
            display += letter
            word.append(guess)
        elif letter in word:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" in display:
        check = False
    else:
        check = True
        print("You win.")