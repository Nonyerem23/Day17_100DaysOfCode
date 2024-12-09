
import random
import getpass

def get_player_choice(player):
    choice = getpass.getpass(f"{player}, enter your choice (r, p, s): ").lower()
    while choice not in ["r", "p", "s"]:
        print("Invalid choice. Please try again.")
        choice = getpass.getpass(f"{player}, enter your choice (r, p, s): ").lower()
    return choice

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "draw"
    elif (player1_choice == "r" and player2_choice == "s") or \
         (player1_choice == "p" and player2_choice == "r") or \
         (player1_choice == "s" and player2_choice == "p"):
        return "Player 1"
    else:
        return "Player 2"

def play_round():
    player1_choice = get_player_choice("Player 1")
    player2_choice = get_player_choice("Player 2")
    return determine_winner(player1_choice, player2_choice)

def play_game():
    player1_score = 0
    player2_score = 0
    rounds = 0

    while True:
        rounds += 1
        print(f"\nRound {rounds}")
        winner = play_round()
        if winner == "Player 1":
            player1_score += 1
            print("Player 1 wins this round!")
        elif winner == "Player 2":
            player2_score += 1
            print("Player 2 wins this round!")
        else:
            print("This round is a draw!")

        print(f"Score: Player 1 {player1_score} - {player2_score} Player 2")
        print()
        while True:
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("\nFinal Score:")
                print(f"Player 1: {player1_score}")
                print(f"Player 2: {player2_score}")

                if player1_score > player2_score:
                    print("Congratulations Player 1! You won the game!")
                elif player2_score > player1_score:
                    print("Congratulations Player 2! You won the game!")
                else:
                    print("The game is a draw!")

                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

if __name__ == "__main__":
    play_game()
