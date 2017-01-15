import copy

def new_board(row, col):
    twod_list = []
    for i in range(0,row):
        oned_list = []
        for j in range(0,col):
            oned_list.append(1)
        twod_list.append(oned_list)
    return twod_list

def count(board,r,c):
    row = len(board)
    col = len(board[1])
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
            if board[element[0]][element[1]] != 0:
                count += 1
    elif r == 0 and c == col - 1:
        for element in [left, low_left, low]:
            if board[element[0]][element[1]] != 0:
                count += 1
    elif r == row - 1 and c == 0:
        for element in [up, right, up_right]:
            if board[element[0]][element[1]] != 0:
                count += 1
    elif r == row - 1 and c == col - 1:
        for element in [left, up, up_left]:
            if board[element[0]][element[1]] != 0:
                count += 1
    elif r == 0:
        for element in [left, right, low, low_left, low_right]:
            if board[element[0]][element[1]] != 0:
                count += 1
    elif r == row - 1:
        for element in [left, right, up, up_left, up_right]:
            if board[element[0]][element[1]] != 0:
                count += 1
    elif c == 0:
        for element in [up, low, right, up_right, low_right]:
            if board[element[0]][element[1]] != 0:
                count += 1
    elif c == col - 1:
        for element in [up, low, left, up_left, low_left]:
            if board[element[0]][element[1]] != 0:
                count += 1
    else:
        for element in elements:
            if board[element[0]][element[1]] != 0:
                count += 1
    return count

def update_board(board):
    num_of_rows = len(board)
    num_of_cols = len(board[1])
    original_board = copy.deepcopy(board)
    for i in range(0,num_of_rows):
        for j in range(0,num_of_cols):
            board[i][j] = count(original_board,i,j)
    counted_board = copy.deepcopy(board)
    for i in range(0,num_of_rows):
        for j in range(0,num_of_cols):
            if counted_board[i][j] > 3 or counted_board[i][j] < 2 and original_board[i][j]:
                board[i][j] = 0 #if an alive cell has more than three or less than two adjacent alive cells, it dies
            elif counted_board[i][j] == 3 and (not original_board[i][j]):
                board[i][j] = 1 #if a dead cell has three alive adjacent cells, it becomes alive
            else:
                board[i][j] = original_board[i][j] + 1 #the value means age, every time self plus 1
    return counted_board
