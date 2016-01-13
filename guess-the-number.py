#import modules that include randomeness, time control, string, and exit element
from random import randint
import string
import time
from sys import exit
import sys,string

#define function that starts the game
def playGame():
        #retrieve the user's guess
        guess = input("What is your guess? Type a number [1 ~ 50]\n: ")

        #if the guess equals the random number, congratulate the user and ask if the user wants to play again.
        if guessMe == guess:
            print "\tCorrect!\n"
            playAgain()

        #if the guess is greater than the random number, tell the user and ask to retry
        elif guessMe < guess:
            print "Too high! Try Again!\n"
            playGame()

        #if the guess is lesser than the random number, tell the user, and ask for retry
        elif guessMe > guess:
            print "Too low! Try Again!\n"
            playGame()

        #if the user typed other than number, ask for valid input
        else:
            print "Invalid input. Please Type a Number 1 to 50.\n "
            playGame()

# define a function for aksing if the user wants to play again
def playAgain():

    #ask yes or no
    choice = raw_input("PLAY AGAIN? [y]\nNo.Exit the program. [n]\n:")

    #if the user typed y, recall rePlay function and play again
    if choice == 'y':
        print "Okay! Let's Play Again!\n"
        rePlay()

    #if the user typed n, say bye and exit the program
    elif choice == 'n':
        print "Exiting the program...\n\nGood Bye!"
        time.sleep(0.5)
        sys.exit()

    #if typed neither y nor n, ask again for a valid input
    else:
        print "Invalid option. Please Type 'y' or 'n'\n"
        playAgain()

# define a function for replay,
def rePlay():

    #assgin new random integer and recall the playGame function
    guessMe=randint(1,50)
    playGame()


#run the functions forever untill interrupted
while True:

    #assgin new random integer
    guessMe =randint(1,50)

    #call playGame function and initiate the game
    playGame()
