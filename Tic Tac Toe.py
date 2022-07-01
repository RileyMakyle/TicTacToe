# Riley Hall
# Tic-Tac-Toe
# 9/13/21
# Program is to setup a game of tic-tac-toe between two users, record the winner (or tie) and then ask to play again.



#list for boxes
boxes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#main function
def main():
    player = 1
    condition = -1

    while condition == -1:
        gameBoard()

# setting up player 1 and player 2
        if player % 2 == 1:
            player = 1
        else:
            player = 2

        print("\nPlayer", player)
        choice = int(input("Enter a number 1 through 9: "))

# assigning symbols (x's and o's)
        if player == 1:
            symbol = "x"
        else:
            symbol = "o"

#if statement for changing the boxes number to player's assigned symbol
        if choice == 1 and boxes[1] == 1:
            boxes[1] = symbol

        elif choice == 2 and boxes[2] == 2:
            boxes[2] = symbol

        elif choice == 3 and boxes[3] == 3:
            boxes[3] = symbol

        elif choice == 4 and boxes[4] == 4:
            boxes[4] = symbol

        elif choice == 5 and boxes[5] == 5:
            boxes[5] = symbol

        elif choice == 6 and boxes[6] == 6:
            boxes[6] = symbol

        elif choice == 7 and boxes[7] == 7:
            boxes[7] = symbol

        elif choice == 8 and boxes[8] == 8:
            boxes[8] = symbol

        elif choice == 9 and boxes[9] == 9:
            boxes[9] = symbol

#error message if player enters something invalid
        else:
            print("Error: Please select a box 1 through 9 ")
            player -= 1

        condition = game_condition()
        player += 1

#print results
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if condition == 1:
        print("Congratulations player", player - 1, "you've won!")
    else:
        print("It's a tie game!")

    replay = input("Would you like to play again?:  y/n     ")
    if replay == "y":
        boxes[1] = 1
        boxes[2] = 2
        boxes[3] = 3
        boxes[4] = 4
        boxes[5] = 5
        boxes[6] = 6
        boxes[7] = 7
        boxes[8] = 8
        boxes[9] = 9


        main()





#function for displaying board
def gameBoard():
    print("\nTic Tac Toe Three in a row!\n")
    print("Player 1 (x's)  -  Player 2 (o's)")
    print()
    print("      |      |      ")
    print(" ", boxes[1], "  | ", boxes[2], "  | ", boxes[3])
    print("______|______|______")
    print("      |      |      ")
    print(" ", boxes[4], "  | ", boxes[5], "  | ", boxes[6])
    print("______|______|______")
    print("      |      |      ")
    print(" ", boxes[7], "  | ", boxes[8], "  | ", boxes[9])
    print("      |      |      ")

#function for win conditions (three ina  row)

def game_condition():


    #horizontal wins
    if boxes[1] == boxes[2] and boxes[2] == boxes[3]:
        return 1
    elif boxes[4] == boxes[5] and boxes[5] == boxes[6]:
        return 1
    elif boxes[7] == boxes[8] and boxes[8] == boxes[9]:
        return 1


    # vertical wins
    elif boxes[1] == boxes[4] and boxes[4] == boxes[7]:
        return 1
    elif boxes[2] == boxes[5] and boxes[5] == boxes[8]:
        return 1
    elif boxes[3] == boxes[6] and boxes[6] == boxes[9]:
        return 1


    # diagonal wins
    elif boxes[1] == boxes[5] and boxes[5] == boxes[9]:
        return 1
    elif boxes[3] == boxes[5] and boxes[5] == boxes[7]:
        return 1


    #endgame + tie
    elif boxes[1] != 1 and boxes[2] != 2 and boxes[3] != 3 and boxes[4] != 4 and boxes[5] != 5 and boxes[
        6] != 6 and boxes[7] != 7 and boxes[8] != 8 and boxes[9] != 9:
        return 0

    else:
        return -1


main()