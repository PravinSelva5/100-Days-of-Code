#Step 1 
import random
import hangman_words
import hangman_art

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list).lower()

# Empty List called display with '_' for each letter of the chose word_list
display = []
for letter in chosen_word:
  display += "_"

# while loop to ask the user to guess again
end_of_game = False
lives = 6

while not end_of_game:
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input("Guess a letter: ")

  if guess in display:
    print(f"You have already guessed {guess}")
  # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  chosen_word_len = len(chosen_word)

  for position in range(chosen_word_len):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter {guess}")

    if chosen_word[position] == guess:
      display[position] = guess
  
  
  if guess not in chosen_word:
    print(hangman_art.stages[lives])
    print(f"You guessed {guess}, that's not in the word, you lose a life")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")
  
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")