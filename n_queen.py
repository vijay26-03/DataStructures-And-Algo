#refered in codesdope
queens = 4
board = [[0 for row in range(queens)] for column in range(queens)]

def is_safe(row, column):
    for k in range(0,queens):
        if board[row][k]==1 or board[k][column]==1:
            return True
    for k in range(0,queens):
        for l in range(0,queens):
            if (k+l==row+column) or (k-l==row-column):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    if n==0:
        return True
    for row in range(0,queens):
        for column in range(0,queens):
            if (not(is_safe(row,column))) and (board[row][column]!=1):
                board[row][column] = 1
                if N_queen(n-1)==True:
                    return True
                board[row][column] = 0

    return False

N_queen(queens)
print(*board,sep='\n')