import random
import re

HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                        """
MAX_TRIES = 6

PICTURE_1 = """x-------x"""

PICTURE_2 = """
x-------x
|
|
|
|
|
"""

PICTURE_3 = """
x-------x
|       |
|       0
|
|
|
"""

PICTURE_4 = """
x-------x
|       |
|       0
|       |
|
|
"""

PICTURE_5 = """
x-------x
|       |
|       0
|      /|\\
|
|
"""

PICTURE_6 = """
x-------x
|       |
|       0
|      /|\\
|      /
|
"""

PICTURE_7 = """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""

pictures = [PICTURE_1, PICTURE_2, PICTURE_3, PICTURE_4, PICTURE_5, PICTURE_6, PICTURE_7]

def is_valid_input(letter_guessed, old_letters_guessed):

  if (len(letter_guessed) != 1 or (not letter_guessed.isascii() or bool(re.search(r'\d', letter_guessed)))):
    return False 
    
  for letter in old_letters_guessed:  #
    if letter == letter_guessed:
      return False 

  return True

def try_update_letter_guessed(hidden_word, letter_guessed, old_letters_guessed):
  if (is_valid_input(letter_guessed, old_letters_guessed)):
    old_letters_guessed.append(letter_guessed)
    if letter_guessed in hidden_word:
      return True

  print("Letters Guessed: ")
  for letter in old_letters_guessed:
    print(letter)

  return False

def show_hidden_word(secret_word, old_letters_guessed):
  result = ""

  for char in secret_word:
    if char in old_letters_guessed:
      result += char
    else:
      result += "_"

  return result

def check_win(secret_word, old_letters_guessed):
  hiddenWordWithOnlyLettersUserGuessed = show_hidden_word(secret_word, old_letters_guessed)

  if not "_" in hiddenWordWithOnlyLettersUserGuessed:
    return True
  
  return False

def choose_word(file_path, index):
  words = []

  file = open(file_path, 'r')

  text = file.read()
  words = text.split(" ")

  return words[index] 

def getFileLength(file_path):

  file = open(file_path, 'r')

  text = file.read()
  words = text.split(" ")

  return len(words) 


def main():
  
  userWantsToPlay = True 

  MAX_TRIES = 6

  print(HANGMAN_ASCII_ART)

  while(userWantsToPlay):

    num_tries = 0 
    input_valid = False

    while (not input_valid):
      try: 
        file_path = (input("Please enter the file and file path from which the word will be taken: "))
        randomWord = input("Do you want a random word from the file? (Y/N)")

        if randomWord == 'Y':
          word_number = random.randrange(1, getFileLength(file_path), 1)

        else:
          word_number = int(input("Please enter the number of the word in the file: ")) - 1

        hidden_word = choose_word(file_path, word_number)
        input_valid = True 
      except: 
        print("Invalid file or file path or their are not enough words in the file")
        input_valid = False

    print("The Word: ")
    print("_" * len(hidden_word))

    userGuessing = True 

    old_letters_guessed = []

    while userGuessing and num_tries <  6:
      letter_guessed = (input("Guess a letter: ")).lower()
      print("\n")

      if is_valid_input(letter_guessed, old_letters_guessed):
          
        if try_update_letter_guessed(hidden_word, letter_guessed, old_letters_guessed):
          print(show_hidden_word(hidden_word, old_letters_guessed))

          if check_win(hidden_word, old_letters_guessed):
            print("GOOD JOB! YOU WON!")
            userGuessing = False 

        else:
          num_tries += 1 
          print("Missed guesses left: " , num_tries, "/", MAX_TRIES, "\n")
          print(pictures[num_tries], '\n')

      elif letter_guessed in old_letters_guessed: 
        print("Please write a new letter")

      else: 
        print("Please write a english letter")

    if num_tries >= 6:
      print("Nice try... Maybe next time")

    userWantsToPlay = (input("Would you like to play again? (Y/N)")) == 'Y' 


if __name__ == '__main__': 
  main()
