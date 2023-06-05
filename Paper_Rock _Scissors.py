import random

options = ("scissors", "rock", "paper")

answer = input("Do you want to play? ")
answer = answer.lower()

while answer == "yes":
    human_choice = input("Please give your choice: ")
    human_choice = human_choice.lower()

    PC_choice = random.choice(options)
    print("Computer chose", PC_choice)

    if PC_choice == human_choice:
        print("draw")
    if human_choice == "scissors" and PC_choice == "paper":
        print("You won")
    if human_choice == "scissors" and PC_choice == "rock":
        print("You lost")
    if human_choice == "paper" and PC_choice == "rock":
        print("You won")
    if human_choice == "paper" and PC_choice == "scissors":
        print("You lost")
    if human_choice == "rock" and PC_choice == "scissors":
        print("You won")
    if human_choice == "rock" and PC_choice == "paper":
        print("You lost")
    else:
        print('You have to choose one of the following: scissors, rock, paper')
    answer = input("Do you want to play again?")
