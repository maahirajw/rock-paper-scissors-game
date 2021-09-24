# game.py

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")

import random
options = ["rock", "paper", "scissors"]

print("Welcome", x, "to my rock-paper-scissors game!")
print ("-------------------")
print("Rock, Paper, Scissors, Shoot!")


#PROMPT USER FOR INPUT 

#x = input ("Choose 'rock' or 'paper' or 'scissors' ")
user_choice = input ("Choose 'rock' or 'paper' or 'scissors' ")
print ("user chose:")
print (user_choice)

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print ("computer chose:")
print (computer_choice)
print ("-------------------")

if (user_choice == 'rock' and computer_choice == 'paper'): 
    print ("oh, the computer won. It's ok")
    print ("-------------------")
elif user_choice == 'paper' and computer_choice == 'scissors': 
    print ("oh, the computer won. It's ok")
    print ("-------------------")
elif user_choice == 'scissors' and computer_choice == 'rock':
    print ("oh, the computer won. It's ok")
    print ("-------------------")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print ("You won. Congratulations!")
    print ("-------------------")
elif user_choice == 'paper' and computer_choice == 'rock': 
    print ("You won. Congratulations!")
    print ("-------------------")
elif user_choice == 'scissors' and computer_choice == 'paper': 
    print ("You won. Congratulations!")
    print ("-------------------")
elif user_choice == 'rock' and computer_choice == 'rock':
    print ("It is a tie.")
    print ("-------------------")
elif user_choice == 'paper' and computer_choice == 'paper': 
    print ("It is a tie.")
    print ("-------------------")
elif user_choice == 'scissors' and computer_choice == 'scissors': 
    print ("It is a tie.")
    print ("-------------------")
else:
    print ("Your choice is invalid.")
    print ("Be sure to check that all your letters are in lowercase!")
    print ("-------------------")


print("Thanks for playing.Hope to see you again!")
print ("-------------------")


#breakpoint()
