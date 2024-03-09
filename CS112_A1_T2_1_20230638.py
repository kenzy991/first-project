#File:CS12_A1_T2_1_20230638.py
#Purpose:Both players start at 0 and add the numbers 1 to 10 to count the player's total winnings until it reaches 100.
#Auther: Kenzy Hamdy Hassan Mohamed
#ID:20230638
# Define the main function
def main():
    # Initialize the score
    score = 0
    # Continue the game until someone reaches 100 points
    while score < 100:
        # Player 1's turn
        while True:  # Keep asking for input until a valid move is provided
            # Ask for input
            move = input("Player 1, enter your move (1-10): ")
            # Check if input consists of digits only
            if move.isdigit():
                move = int(move)
                # Check if the move is valid
                if 1 <= move <= min(10, 100 - score):
                    score += move  # Update the score
                    if score > 100:  # Check if the score exceeds 100
                        print("Player 1's move causes the score to exceed 100. Please enter a smaller move.")
                        score -= move  # Undo the invalid move
                    elif score == 100:  # Check if Player 1 has won
                        print("Player 1 is the winner!")
                        break  # Exit the loop if Player 1 has won
                    else:
                        print("Current score:", score)  # Display the current score
                    break  # Break out of the while loop for Player 1's turn
                    # Invalid move message
                else:
                    print(f"Invalid move. Please enter a number between 1 and {min(10, 100 - score)}.")
            else:
                print("Invalid input. Please enter a digit between 1 and 10.")  # Input consists of non-digits

        if score >= 100:  # Check if Player 1 has won before proceeding to Player 2's turn
            break

        # Player 2's turn
        while True:  # Keep asking for input until a valid move is provided
            move = input("Player 2, enter your move (1-10): ")  # Ask for input
            if move.isdigit():  # Check if input consists of digits only
                move = int(move)
                if 1 <= move <= min(10, 100 - score):  # Check if the move is valid
                    score += move  # Update the score
                    if score > 100:  # Check if the score exceeds 100
                        print("Player 2's move causes the score to exceed 100. Please enter a smaller move.")
                        score -= move  # Undo the invalid move
                    elif score == 100:  # Check if Player 2 has won
                        print("Player 2 is the winner!")
                        break  # Exit the loop if Player 2 has won
                    else:
                        print("Current score:", score)
                    break  # Break out of the while loop for Player 2's turn
                else:
                    # Invalid move message
                    print(f"Invalid move. Please enter a number between 1 and {min(10, 100 - score)}.")
            else:
                # Input consists of non-digits
                print("Invalid input. Please enter a digit between 1 and 10.")


# Execute the main function
if __name__ == "__main__":
    main()
