import random

# Rock
rock = ("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

# Paper
paper = ("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

# Scissors
scissors = ("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

graphics = [rock, paper, scissors]

#game logic
def who_wins(player_choice, computer_choice) -> str:
    
    if player_choice >= 3 or player_choice < 0:
        result = print("Invalid number! You lose!")
    elif player_choice == 0 and computer_choice == 2:
        result = print("You win!")
    elif computer_choice == 2 and player_choice == 0:
        result = print("You lose!")
    elif computer_choice > player_choice:
        result = print("You lose!")
    elif player_choice > computer_choice:
        result = print("You win!")
    elif player_choice == computer_choice:
        result = print("It's a draw!")
    return result

# game process
player_choice = int(input("What do you choose? Type 0 = Rock, 1 = Paper, 2 = Scissors!\n"))
print(f"You choose {player_choice}!")
if player_choice <= 2:
    print(graphics[player_choice])
    computer_choice = random.randint(0,2)
    print(f"Computer choose {computer_choice}!")
    print(graphics[computer_choice])
    #result!
    who_wins(player_choice,computer_choice)
else:
    print("GAME OVER! YOU CANT FOLLOW THE RULES!")