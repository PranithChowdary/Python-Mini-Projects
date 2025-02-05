# Author : Pranith Chowdary K
# Date   : 05-01-2020
# Github : https://github.com/PranithChowdary 
# Tags   : Short, Game, Puzzle

""" In Bagels, a deductive logic game, you
must guess a secret three-digit number
based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the
wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess
has no correct digits. You have 10 tries to guess the
secret number. """


import random

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10
MAX_GUESSES = 10 # (!) Try setting this to 1 to 100.

def main():
    """ Main function """
    print("""\n\tBagels, a deductive logic game.\n
          
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        When I say:     That means:
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct.

        For example, if the secret number was 248 and your guess was 843, 
        the clues would be Fermi Pico.\n\n""".format(NUM_DIGITS))
    
    while True: # Main Game loop
        # This stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
               
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep loop until they enter a valid guess:
            while len(guess)!= NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
        
            if guess == secretNum:
                break # They're correct so break out of the loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))
                
        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for Playing..!')
    
def getSecretNum():
    """ Returns a  string made up of NUM_DIGITS unique random digits."""
    
    numbers = list('0123456789') # Create a list of digits 0 to 9
    random.shuffle(numbers) # Shuffle them into random order
    
    # Get the first NUM_DIGITS digit in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):    
    """Returns a string with the pico, fermi, bagels clues for a guess 
    and secret number pair."""
    
    if guess == secretNum:
        return 'You got it..!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            # A correct digit is in the wrong place.
            clues.append('Pico ')
    
    if len(clues) == 0:
        return 'Bagels '
    # There are no correct digits at all
    else:
        # Short the clues in alphabetical order so their original order
        # doesn't give any infromation.
        clues.sort()
        # Make a single string from the list of string clues.
        return ''.join(clues)
    
if __name__ == '__main__':
    main()