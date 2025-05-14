import random

def play_rock_paper_scissors():
    """Plays a single round of Rock, Paper, Scissors."""

   
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    
    computer_choice = random.choice(["rock", "paper", "scissors"])


    print(f"You chose {player_choice}, computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")


while True:
    play_rock_paper_scissors()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")