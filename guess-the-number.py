from random import randint
import string
import time
from sys import exit


while True:
    print "\tGuess A Number Between 1 to 50!\n"

    guessMe = randint (1,50)

    guess = input("What is your guess? Type a number [1 ~ 50] : ")
    while True:
        if guessMe == guess:
            print "Correct! \n"

            while True:
                choice = raw_input("Do you want to play again? Type [y/n] :")
                if choice == 'y':
                    print "Okay! Let's Play Again!\n"
                elif choice == 'n':
                    sys.exit()
                else:
                    print "Invalid option. Please Type 'y' or 'n'"

        elif guessMe < guess:
                print "Too high! Try Again!\n"

        elif guessMe > guess:
            print "Too low! Try Again!\n"

        else:
            print "Invalid input. Please Type a Number 1 to 50 "
