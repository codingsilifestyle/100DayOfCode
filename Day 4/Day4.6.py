#The game is Rock Paper Scissors
#A player can play either rock, paper or scissors.
#The computer will randomly choose one of these three options and the winner is determined by
import random
UserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
Ran = [Rock,Paper,Scissors]
ComputerChoice =  random.randint(0,2) 
print(f"Your Choice is {UserChoice}: \n {Ran[UserChoice]} \n Computer Choice is {ComputerChoice}: {Ran[ComputerChoice]} ")
if UserChoice == ComputerChoice : 
    print("Try again")
elif (UserChoice == 0) and (ComputerChoice == 1) :
    print("You Lose")
elif ((UserChoice == 0) and (ComputerChoice == 2) ):
    print("You Win")
    # comment:     
elif (UserChoice == 1) and (ComputerChoice == 0) :
    print("You Win")
elif ((UserChoice == 1) and (ComputerChoice == 2) ):
    print("You Lose")
elif (UserChoice == 2) and (ComputerChoice == 0) :
    print("You Lose")
elif ((UserChoice == 2) and (ComputerChoice == 1) ):
    print("You Win")

    # comment:     