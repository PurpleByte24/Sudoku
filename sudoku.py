import tkinter as tk
import backtrackingAlgorithm as btA


root = tk.Tk()
root.title("Sudoku")
root.minsize(600, 600)
root.maxsize(600, 600)

## GUI
frames = [[tk.Frame(root, highlightbackground="black", highlightthickness=2) for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        frames[r][c].grid(row=r, column=c) 

def generateCells(board):
    cells = []
    for row in range(9):
        for col in range(9):
            frameIndex_r = row // 3
            frameIndex_c = col // 3
            
            cell = tk.Button(frames[frameIndex_r][frameIndex_c],
                             height = 2,
                             width = 1, 
                             text="")
            cell.grid(row=row, column=col)
            cells.append(cell)
    showCellNums(cells, board)

def showCellNums(cells, board):
    for Index, cell in enumerate(cells):
        cells[Index].config(text=board[Index])

def main():
    board = btA.generateSudoku()
    generateCells(board)

main()

root.mainloop()