from random import randint
import string
import time
from sys import exit
import sys,string


def playGame():
        #retrieve the user's guess
        guess = input("What is your guess? Type a number [1 ~ 50]\n: ")

        if guessMe == guess:
            print "\tCorrect!\n"
            playAgain()

        elif guessMe < guess:
            print "Too high! Try Again!\n"
            playGame()

        elif guessMe > guess:
            print "Too low! Try Again!\n"
            playGame()

        else:
            print "Invalid input. Please Type a Number 1 to 50.\n "
            playGame()

def playAgain():
    choice = raw_input("PLAY AGAIN? [y]\nNo.Exit the program. [n]\n:")
    if choice == 'y':
        print "Okay! Let's Play Again!\n"
        rePlay()
    elif choice == 'n':
        print "Exiting the program...\n\nGood Bye!"
        time.sleep(0.5)
        sys.exit()
    else:
        print "Invalid option. Please Type 'y' or 'n'\n"
        playAgain()

def rePlay():
    guessMe=randint(1,50)
    playGame()


while True:
    guessMe =randint(1,50)
    playGame()
