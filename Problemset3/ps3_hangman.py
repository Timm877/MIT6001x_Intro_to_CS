# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    goodguesses = 0
    alreadyGuessed= []
    
    for i in lettersGuessed:
        if i in alreadyGuessed:
            goodguesses += 0 
        else:    
            goodguesses += secretWord.count(i)
            alreadyGuessed.append(i)       
    return goodguesses == len(secretWord)

#below was my first code which did not include more occurences of same guess in secretword.
# goodguesses = 0
#     for i in lettersGuessed:
#         if i in secretWord:
#             goodguesses +=1
#     return goodguesses == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = []            
    for i in secretWord:
        if i in lettersGuessed:
            guessedWord.append(i)
        else:
            guessedWord.append('_ ')
    guessedWord = "".join(guessedWord)
    
    return guessedWord        
        


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    new_abc = []    
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            new_abc.append(i)
            
    return ''.join(new_abc)    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the amazing game Hangman.")
    print("I am thinking of a word with a length of " + str(len(secretWord)) + " letters.")
    
    remainingGuesses = 8
    lettersGuessed = []
    import string
    
    while remainingGuesses > 0:
        
        if getGuessedWord(secretWord,lettersGuessed) == secretWord:
            break
        print("-------------------------")
        print("You have " + str(remainingGuesses) + " guesses left.")
        
        
        
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        userGuess = input("Please guess a letter:")
        userGuess = userGuess.lower()
        
        if userGuess in string.ascii_lowercase:
            if userGuess in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(userGuess)
                getGuessedWord(secretWord,lettersGuessed)
                
                if userGuess in secretWord:
                    print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                else:
                    print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord,lettersGuessed))
                    remainingGuesses -= 1
        else:
            print("Your guess is invalid. Please try again.")            
    
    print("-------------------------")
    if remainingGuesses == 0:
        return print("LOSER! The word was " + secretWord)
    else:
        return print("Congratulations, you won!")
        



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretword)

# print(isWordGuessed('aap',['a','p','a']))

# print(getGuessedWord('aap',['a']))

# print(getAvailableLetters(['a','g','x']))