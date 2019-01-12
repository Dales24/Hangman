import time
import random
import sys

name = raw_input("What is your name?")

print "Hey," + name, "Welcome to hangman!"

print ""

time.sleep(0.5)


def hangman():

    print "guess the word :)"
    print "please only enter lower case letters!!!"

    time.sleep(0.5)

    yes = "yes"

    words = ["secret", "coding", "software", "python", "program"]

    word = random.choice(words)

    guesses = ''

    turns = 10


    while turns > 0:

        failed = 0
        
        for char in word:

            if char in guesses:
        
                print char,

            else:
        
                print "_",
           
                failed += 1

        if failed == 0:
           
           print "Winner!!!"
        
  
           response = raw_input("Enter yes to play again: ")
    

           if response == yes:
                    
                hangman()

           break

        print

        while True:
          guess = raw_input("guess a character:")
          if len(guess) == 1 and not guess.isdigit() :
            guessInLower = guess.lower()
            guesses += guessInLower
            break
          else:
            print("Oops!  That was not a valid entry. 0nly lower case leters.  Try again...")

        if guess not in word:
     
            turns -= 1
     
            print "Wrong"
     
            print "You have", + turns, 'guesses'
     
            if turns == 0:
        
                print "You Loose, want to play again?"

                response = raw_input("Enter yes to play again: ")

                if response == yes:

                    hangman()

                break


hangman()



