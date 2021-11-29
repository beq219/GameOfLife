from random import random
from pprint import pprint as pp

# Two States: Dead , Alive
# neighborhood: the 8 cells surrounding target cell
# with every iteration, evaluate each cell to determine new state based on neighborhood
# Rules:
#   underpopulation: any live cell with fewer than 2 live neighbors dies            State: 1 -> 0
#   overpopulation: any live cell with more than 3 live neighbors dies              State: 1 -> 0
#   reproduction: any dead cell with exactly 3 live neighbors become a live cell    State: 0 -> 1
#   any live cell with 2 or 3 live neighbors live on to the next generation         State: 1 -> 1
# TODO: create 2D array with each cell being a random state: 1 or 0

def createTable(col: int=10, row: int=10):
    # first create table with empty value
    # table = [[0 for i in range(col)] for j in range(row)]
    # then fill the table randomly with 1 or 0
    # for i in range(col):
    #     for j in range(row):
    #         table[i][j] = random().__round__()
    # print(table[9][8])

    # access table through table[row][col]

    table = [[random().__round__() for i in range(col)] for j in range(row)]
    return table


def main():
    test = createTable()
    pp(test)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
