# game.py

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")

import random
options = ["rock", "paper", "scissors"]

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

if (user_choice == 'rock' and computer_choice == 'paper'): 
    print ("oh, the computer won. It's ok")
elif user_choice == 'paper' and 'computer_choice' == 'scissors': 
    print ("oh, the computer won. It's ok")
elif user_choice == 'scissors' and computer_choice == 'rock':
    print ("oh, the computer won. It's ok")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print ("You won. Congratulations!")
elif user_choice == 'paper' and computer_choice == 'rock': 
    print ("You won. Congratulations!")
elif user_choice == 'scissors' and computer_choice == 'paper': 
    print ("You won. Congratulations!")
elif user_choice == 'rock' and computer_choice == 'rock':
    print ("It is a tie.")
elif user_choice == 'paper' and computer_choice == 'paper': 
    print ("It is a tie.")
elif user_choice == 'scissors' and computer_choice == 'scissors': 
    print ("It is a tie.")


print("THANKS PLEASE PLAY AGAIN")

#breakpoint()



