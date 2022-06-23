
import random
#Define the size of the board
size = 10
#Create a first random board
board = [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

#Define a function for printng the boards
def board_print(board, size):
    for i in range(size+2):
        for j in range(size+2):
            if i == 0 or i == size+1:
                if not(j == size+1):
                    print("-", end="")
                else:
                    print("-")
            else:
                if j == 0:
                    print("|", end="")
                elif j == size+1:
                        print("|")
                else:
                    if board[i-1][j-1] == 0:
                        print(" ", end= "")
                    elif board[i-1][j-1] == 1:
                        print("X", end= "")

#Define a function for counting the alive neighbours that each cell has
def alive_neighbours(board, x, y, size):
    alive = 0
    #Iterate through the different positions of the neighbours
    for k in (x, x - 1, x + 1):
        for z in (y, y - 1, y + 1):
            #Skip when it marks the position of the cell
            if not (k == x and z == y):
                #Only count them if the position is in range
                if k >= 0 and k < size and z >= 0 and z < size:
                    if board[k][z] == 1:
                        alive += 1
    #Return the number of alive neighbours
    return alive

#Define a function to compute the next board
def next_board(board, size):
    #Generate the next board, composed by 0s
    nextboard = [[0 for _ in range(size)] for _ in range(size)]
    #Count the number of neighbours for every position of the board
    for x in range(size):
        for y in range(size):
            alive = alive_neighbours(board, x, y, size)
            #Apply the rules of the game of life and modify the next board accordingly
            if board[x][y] == 1:
                if alive < 2 or alive > 3:
                    nextboard[x][y] = 0
                else:
                    nextboard[x][y] = 1
            else:
                if alive == 3:
                    nextboard[x][y] = 1
                else:
                    nextboard[x][y] = 0
    board_print(nextboard, size)
    return nextboard

#Print the first board
board_print(board, size)

while True:
    #Ask the user if they want to continue the simulation
    print("Continue simulation (y/n)?")
    x = input()
    #If the answer is no, break the loop
    if x == "n":
        break
    #If the answer is yes,
    #compute the next board and save the next board in the variable board
    else:
        board = next_board(board, size)