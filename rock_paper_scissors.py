import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True: 
    #Asking the user to type in rock, paper, or scissors
    user_input = input("Type Rock/Paper/Scissors or X to quit: ").lower()
    #Quitting the program if the user enters in "x"
    if user_input == "x":
        break

    #If the user does not input one of these words then it will prompt them again
    if user_input not in choices:
        continue

    #generates a random number from 0-2
    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, rock: 2

    computer_choice = choices[random_num]
    print("Computer chooses:", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won")
        user_wins += 1
        continue

    if user_input == "scissors" and computer_choice == "paper":
        print("You won")
        user_wins += 1
        continue
    
    if user_input == "paper" and computer_choice == "rock":
        print("You won")
        user_wins += 1
        continue

    else: 
        print("You lost")
        computer_wins += 1
        continue



print("Goodbye!")