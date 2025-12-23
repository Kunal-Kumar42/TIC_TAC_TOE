import next_move
import random
import pandas as pd

df = pd.read_csv("my_tic_tac_toe_all.csv")

def printmatrix(matrix):
    print(f" {matrix[0]} | {matrix[1]} | {matrix[2]} ")
    print("-----------")
    print(f" {matrix[3]} | {matrix[4]} | {matrix[5]} ")
    print("-----------")
    print(f" {matrix[6]} | {matrix[7]} | {matrix[8]} ")

# Victory positions
victorycode = [
    [0,1,2],[3,4,5],[6,7,8],  # rows
    [0,3,6],[1,4,7],[2,5,8],  # columns
    [0,4,8],[2,4,6]           # diagonals
]

# Instructions
print("\n\n       TIC-TAC-TOE GAME       \n")
print("________RULE________\n")
print("3x3 grid is numbered 0-8. Type the position number to place X or O.\n")

# initializing variables
matrix_real = [" "]*9
matrix_show = list(range(9))
printmatrix(matrix_show)
mode = 3

# mode game mode
while(mode < 4):
    mode-=1
    #mode selection
    print("\nMode:\n1. Two player\n2. Single player")
    choice = int(input("\nEnter your choice: "))

    while(mode<3):
        mode-=1
        #name choice
        name1 = input("Enter first player name: ")
        if choice == 1:
            name2 = input("Enter second player name: ")
        else:
            name2 = "Bot"

        while(mode<2):
            mode-=1
            # initializing score variable 
            player1 = []   # to store player1 entered cell name
            player2 = []   # to store player1 entered cell name
            matrix_real = [" "]*9    # to show current status of matrix

            # starting game
            status = "finding"         # finding end of match
            winner = None               #no winner till now
            move = 0               # 0 move till now

            while status == "finding" and move < 9:

                # Player 1 move
                while True:
                    p1 = int(input(f"{name1}'s Turn : "))
                    if p1 not in player1 + player2 and 0 <= p1 <= 8:
                        break
                    print("Invalid move! Try again.")
                player1.append(p1)
                matrix_real[p1] = "X"
                print("\n")
                printmatrix(matrix_real)
                print("\n")

                # Check if player 1 wins
                for el in victorycode:
                    if all(item in player1 for item in el):
                        status = "found"
                        winner = name1
                        break
                if status == "found": break
                move += 1
                if move >= 9: break

                # Player 2 move
                if choice == 1:
                    while True:
                        p2 = int(input(f"{name2}'s Turn : "))
                        if p2 not in player1 + player2 and 0 <= p2 <= 8:
                            break
                        print("Invalid move! Try again.")
                else:
                    print("Bot's Turn ")
                    p2 = next_move.predict(df, player1, player2, 'O')
                    if p2 == '-':
                        valid_nums = [n for n in range(9) if n not in player1 + player2]
                        p2 = random.choice(valid_nums)

                player2.append(p2)
                matrix_real[p2] = "O"
                print("\n")
                printmatrix(matrix_real)
                print("\n")

                # Check if player 2 wins
                for el in victorycode:
                    if all(item in player2 for item in el):
                        status = "found"
                        winner = name2
                        break
                if status == "found": break
                move += 1

            # Result
            if status == "found":
                print(f"\nWinner: {winner}")
            else:
                print("Oops!! Draw")

            print("\nWant to \n")
            print("4. Exit\n3. Change Game Mode \n2.Change Player Name \n1. Play Again  \n")
            mode = int(input("Enter Your desired otion number : "))