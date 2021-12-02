from random import random
from pprint import pprint as pp
import tkinter as tk
import time


# Two States: Dead , Alive
# neighborhood: the 8 cells surrounding target cell
# with every iteration, evaluate each cell to determine new state based on neighborhood
# Rules:
#   underpopulation: any live cell with fewer than 2 live neighbors dies            State: 1 -> 0
#   overpopulation: any live cell with more than 3 live neighbors dies              State: 1 -> 0
#   reproduction: any dead cell with exactly 3 live neighbors become a live cell    State: 0 -> 1
#   any live cell with 2 or 3 live neighbors live on to the next generation         State: 1 -> 1


def create_table(col: int = 10, row: int = 10):
    # create table with either 1 or 0 in each cell using list comprehension
    # access table by table[row][col]
    return [[round(random()) for i in range(col)] for j in range(row)]


def draw_label(root, table, col, row):
    print(f"row: {row}, col: {col}")
    for i in range(col):
        for j in range(row):
            # label = tk.Label(root, text=table[i][j])
            label = tk.Label(root, text="   ")
            label.grid(row=i, column=j)
            if table[i][j]:
                label.config(bg="#000000")
            else:
                label.config(bg="#fff")


def draw_table(col, row):
    root = tk.Tk()
    table = create_table(col, row)
    pp(table)

    # create a label for each cell in grid
    # for i in range(10):
    #     for j in range(10):
    #         tk.Label(root, text=table[i][j]).grid(row=i, column=j)
    draw_label(root=root, table=table, col=col, row=row)
    root.update()
    time.sleep(3)
    # for i in range(10):
    #     for j in range(10):
    #         label = tk.Label(root, text="X")
    #         label.grid(row=i, column=j)

    root.update()

    root.mainloop()


def main():
    # test = create_table()
    # pp(test)
    draw_table(col=20, row=20)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
