from click import open_file


import random

hang = ["""
H A N G M A N - Chad Fike

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Chad Fike

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Chad FIke

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Chad Fike

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Chad Fike

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Chad Fike

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Chad Fike

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():
    word = random.choice(open("hangman.txt").read().split())
    return word


def getGuess(usedGuess):
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        
        if len(guess) != 1:
            print("Please enter just a single letter")
        elif guess in usedGuess:
            print("You already guessed that letter! Try again")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please return a letter")
        else:
            return guess
            
def displayGame(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()
    
    print('Missed Letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print('\n')
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)): #replace blanks with appropraite letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
            
    for letter in blanks:
        print(letter, end = ' ')
    print('\n')
    
def playAgain():
    return input("Do you want to play again?").lower().startswith('Y')
        
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False



while True:
    displayGame(hang, missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("\n" + "Congratsulations! The secret word was " + secretWord)
            gameIsDone = True
            
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(hang) - 1:
            displayGame(hang, missedLetters, correctLetters, secretWord)
            print("Sorry! You have run out of gusses :(" + "\n" + "The secret word was " + "'" + secretWord + "'")
            gameIsDone = True 
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break