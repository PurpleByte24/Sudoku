import tkinter as tk

root = tk.Tk()
root.title("Sudoku")
root.minsize(600, 600)
root.maxsize(600, 600)

frames = [[tk.Frame(root, highlightbackground="black", highlightthickness=2) for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        frames[r][c].grid(row=r, column=c) 


def generateCells():
    for row in range(9):
        for col in range(9):
            frameIndex_r = row // 3
            frameIndex_c = col // 3
            print(f"Row: {row}, Col: {col}")
            
            cell = tk.Button(frames[frameIndex_r][frameIndex_c],
                             height = 2,
                             width = 1, 
                             text="")
            cell.grid(row=row, column=col)

generateCells()

root.mainloop()