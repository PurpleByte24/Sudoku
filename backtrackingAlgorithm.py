def isValid(board, row, col, num):
    for i in range(9): #so every row and col gets checked
        if board[row][i] == num or board[i][col] == num: #check horizontically and vertically 
            return False
    
    startRowInd = 3 * (row // 3) #index of the first row in a set, if you look at the 9 rows in 3x3 sets
    startColInd = 3 * (col // 3) #index of the first cols in a set, if you look at the 9 cols in 3x3 sets

    for r in range(startRowInd, startRowInd + 3): #check if there already is this number in the current 3x3 grid
        for c in range(startColInd, startColInd + 3):
            if board[r][c] == num:
                return False
            
    return True #return True if it is valid

def solveSudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: #so nothing solved gets overridden
                for num in range(1, 10): #check numbers 1 - 9 nine times to see which one fits
                    if isValid(board, row, col, num):
                        board[row][col] = num #put the number in the cell
                        if solveSudoku(board):
                            return True #check the board again for the next cell
                        board[row][col] = 0 #if the Sudoku is unsolvable like this, reset the cell to 0 and try another number
                return True
    return True        

def generateSudoku():
    board = [[0] * 9 for _ in range(9)]
    solveSudoku(board)
    return board