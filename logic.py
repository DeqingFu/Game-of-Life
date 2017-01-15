import copy
import math
import random

"""
create a new board with a random spawn point, given its row and column
row: int
col: int
return: int[][]
"""

initial_row = 7
initial_col = 7
def new_board(row, col): # a 2d array
    twod_list = []
    for i in range(0,row):
        oned_list = []
        for j in range(0,col):
            oned_list.append(0)
        twod_list.append(oned_list)
    return twod_list

# initialize the board
board = new_board(initial_row, initial_col)

# initialze the board for player 1
def initial_player1():
    rand_row_1 = math.trunc(random.random() * len(board))
    rand_col_1 = math.trunc(random.random() * len(board[0]))
    board[rand_row_1][rand_col_1] = 1
    return board

# Player 1 take the move

# after plater 1's move, initialze player 2
def initial_player2():
    rand_row_2 = math.trunc(random.random() * len(board))
    rand_col_2 = math.trunc(random.random() * len(board[0]))
    if board[rand_row_2][rand_col_2] == 1:
        initial_player2()
    else:
        board[rand_row_2][rand_col_2] = 2
    return board

initial_player1()
#player 1 's move
initial_player2()
print board


'''
given a board and a set of row and column,
returns the number of cells surrounding it
board: int[][]
r: int
c: int
return: int
'''
def count_by_player(board,r,c,player):
    row = len(board)
    col = len(board[0])
    up = (r - 1, c )
    low = (r + 1, c )
    left = (r , c - 1)
    right = (r , c + 1)
    up_left = (r - 1, c - 1)
    up_right = (r - 1, c + 1)
    low_left = (r + 1, c - 1)
    low_right = (r + 1, c + 1)
    elements = [up, low, left, right, up_left, up_right, low_left, low_right]
    count = 0
    if r == 0 and c == 0:
        for element in [right, low_right, low]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif r == 0 and c == col - 1:
        for element in [left, low_left, low]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif r == row - 1 and c == 0:
        for element in [up, right, up_right]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif r == row - 1 and c == col - 1:
        for element in [left, up, up_left]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif r == 0:
        for element in [left, right, low, low_left, low_right]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif r == row - 1:
        for element in [left, right, up, up_left, up_right]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif c == 0:
        for element in [up, low, right, up_right, low_right]:
            if board[element[0]][element[1]] == player:
                count += 1
    elif c == col - 1:
        for element in [up, low, left, up_left, low_left]:
            if board[element[0]][element[1]] == player:
                count += 1
    else:
        for element in elements:
            if board[element[0]][element[1]] == player:
                count += 1
    return count

"""
update the status of a given board, according to the rule of the game
board: int[][]
return: int[][]
"""
def update_board(board):
    row = len(board)
    col = len(board[0])
    original_board = copy.deepcopy(board)
    for i in range(0,row):
        for j in range(0,col):
            if board[i][j] == 1:
                board[i][j] = (count_by_player(original_board,i,j,1),1)
                #the first element is the counted number of alive cells of the same player, the second element denotes the player
            elif board[i][j] == 2:
                board[i][j] = (count_by_player(original_board,i,j,2),2)
            else:
                if count_by_player(original_board,i,j,1) == 3:
                    if count_by_player(original_board,i,j,2) ==3:
                        board[i][j] = (0, 0) #annihilization
                    else:
                        board[i][j] = (3, 1)
                elif count_by_player(original_board,i,j,2) ==3:
                    board[i][j] = (3, 2)
                else:
                    board[i][j] = (0, 0) #default value, dead
    counted_board = copy.deepcopy(board)
    for i in range(0,row):
        for j in range(0,col):
            if counted_board[i][j][0] > 3 or counted_board[i][j][0] < 2 and original_board[i][j] != 0:
                board[i][j] = 0 #if an alive cell has more than three or less than two adjacent alive cells, it dies
            else:
                board[i][j] = counted_board[i][j][1] #if a dead cell has three alive adjacent cells, it becomes alive
    return board

'''
#test case
#print(new_board(5,5)) #ok
#print(new_board(2,3)) #ok
#static
bd1 = [[0,0,0,0,0],[0,0,1,1,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
#print(count(bd1,1,2)) #ok
print(update_board(bd1))
#oscillate
bd2 = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
print(update_board(bd2))
#gilder

test_board = [[0,0,0,0,0],[0,1,0,2,0],[0,1,0,2,0],[0,1,0,2,0],[0,0,0,0,0]]
update_board(test_board)
print test_board
'''
