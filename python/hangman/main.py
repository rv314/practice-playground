import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

# Program will choose random word from list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initial params
end_of_game = False
lives = 6

# Print game logo
print(logo)
# Print the chosen word from list
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You have already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed letter '{guess}' which is not in the list. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print relevant stage of life
    print(stages[lives])