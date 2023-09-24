#!/usr/bin/env python3

import os
import random


word_list = [
    "giraffe",
    "elephant",
    "kangaroo",
    "koala",
    "panda",
    "cheetah",
    "leopard",
    "rabbit",
    "squirrel",
    "horse",
    "turkey",
    "penguin",
    "ostrich",
    "peacock",
    "parrot",
    "eagle",
    "seagull",
    "dolphin",
    "whale",
    "shark",
    "octopus",
    "jellyfish",
    "turtle",
    "crocodile",
    "snake",
    "lizard",
    "dolphin",
    "whale",
    "shark",
    "octopus",
    "jellyfish",
    "turtle",
    "crocodile",
    "giraffe",
    "elephant",
    "kangaroo",
    "koala",
    "anteater",
    "cheetah",
    "leopard",
    "rabbit",
    "squirrel",
    "horse",
    "turkey",
    "penguin",
    "ostrich",
    "peacock",
    "parrot",
    "eagle"]


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


rerun = True

while rerun == True:
    chosen_word = random.choice(word_list)
    
    blanks = []
    wrong = []
    
    for _ in chosen_word:
        blanks.append('_')
    
    lives = 6
    
    print(logo) 
    print('Hint: Animal')  
    print(stages[lives])
    for item in blanks:
        print(item, end = ' ')   
    
    end_game = False 
    while not end_game:  
          
        guess = input('\nGuess a letter: ').lower()
        
        os.system('cls' if os.name == 'nt' else 'clear')       
        
        if guess.isalpha() is False:
            print('\n\n\nERROR: Only letters are allowed! Please try again.')       
        elif len(guess)>1:
            print('\n\n\nERROR: Only 1 letter is allowed at a time. Please try again.')
        elif guess in blanks:
            print(f'''\n\nNOTE: You've already chosen the letter {guess}." Please try again!''')  
        else:                          
            if guess in chosen_word:
                print(f'''\n\nYes, "{guess}" is correct!''')
                for char in range(len(chosen_word)):
                    letter = chosen_word[char]
                    if letter == guess:
                        blanks[char] = letter 
            elif guess in wrong:
                print(f'''\n\nNOTE: You've already chosen the letter "{guess}." Please try again!''')                 
            else:
                print(f'''\n\nSorry, "{guess}" isn't right!''')
                lives -= 1
                wrong.append(guess)
       
        print('\n')
        formatted_wrong = ' , '.join(wrong)
        print(formatted_wrong)
        print(stages[lives])
        for item in blanks:
            print(item, end = ' ')
    
        if lives == 0:
            end_game = True
            print(f'\n\nYOU LOSE...\nthe word was: {chosen_word}')    
        elif '_' in blanks: 
            end_game = False
        else:
            end_game = True
            print('\n\nYOU WIN! Nice job.')
    
    redo = input('Enter 9 to play again.\n')
    if redo == '9':
        rerun = True
    else:
        print('\nThanks for playing!')
        rerun = False
        
        



