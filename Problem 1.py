# Declare pairsToCheck globally
pairs_to_check = [[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]]

# Function to check if any pair exists in the list
def check_pairs(numbers_list):
    for pair in pairs_to_check:
        pair_exists = all(num in numbers_list for num in pair)
        if pair_exists:
            return True
    return False

def main():
    numbers_list1 = []
    numbers_list2 = []
    chosen = [False] * 10
    sum1 = 0
    sum2 = 0
    print("Welcome to Number Scrabble.")
    print("The list of numbers is between 1 and 9.")

    # Input numbers
    while True:
        num = int(input("Player 1, please choose a number from the list: "))
        if num < 1 or num > 9 or chosen[num]:
            print("Player 1: Please choose a valid number between 1 and 9 that hasn't been chosen before.")
            continue
        chosen[num] = True
        numbers_list1.append(num)
        sum1 += num
        print("the sum1= ", sum1)
        # Check if any pairs exist for player 1
        if len(numbers_list1) >= 3 and check_pairs(numbers_list1) and sum1 == 15:
            print("Player 1 is the winner.")
            break

   num = int(input("Player 2, please choose a number from the list: "))
        if num < 1 or num > 9 or chosen[num]:
            print("Player 2: Please choose a valid number between 1 and 9 that hasn't been chosen before.")
            continue
        chosen[num] = True
        numbers_list2.append(num)
        sum2 += num
        print("the sum1= ", sum2)
        # Check if any pairs exist for player 2
        if len(numbers_list2) >= 3 and check_pairs(numbers_list2) and sum2 == 15:
            print("Player 2 is the winner.")
            break
        # Check if all numbers are used and no player gets exactly 15
        if len(numbers_list1) + len(numbers_list2) == 9 and sum1 != 15 and sum2 != 15:
            print("The game is a draw.")
            break