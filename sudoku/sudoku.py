"""
This program takes a sudoku grid as an input and solves it
"""
import math

#constants
__VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_grid(grid):
    for i in range(len(grid)):
        print(grid[i])

def is_solved(grid):
    solved = True
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] == 0):
                solved = False
                break
    return solved

def get_unknowns(grid):
    unknowns = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == 0):
                index = []
                index.append(i)
                index.append(j)
                unknowns.append(index)
    return unknowns

def search_area_possible_values(grid,index, possible_vals):
    row = index[0]
    col = index[1]
    for i in range(row,row+3):
        for j in range(col,col+3):
            if grid[i][j] in possible_vals:
                possible_vals.remove(grid[i][j])
    return(possible_vals)

def find_search_area_possible_values(grid, index, possible_vals):
    row = index[0]
    col = index [1]
    if(row < 3):
        if(col < 3):
            possible_vals = search_area_possible_values(grid, [0,0], possible_vals)
        elif(col < 6):
            possible_vals = search_area_possible_values(grid, [0,3], possible_vals)
        else:
            possible_vals = search_area_possible_values(grid, [0,6],possible_vals)
    elif(row < 6):
        if(col < 3):
            possible_vals = search_area_possible_values(grid, [3,0],possible_vals)
        elif(col < 6):
            possible_vals = search_area_possible_values(grid, [3,3],possible_vals)
        else:
            possible_vals = search_area_possible_values(grid, [3,6],possible_vals)
    else:
        if(col < 3):
            possible_vals = search_area_possible_values(grid, [6,0],possible_vals)
        elif(col < 6):
            possible_vals = search_area_possible_values(grid, [6,3],possible_vals)
        else:
            possible_vals = search_area_possible_values(grid, [6,6],possible_vals)
    return possible_vals

def find_possible_values(grid, index):
    possible_vals = __VALUES
    row = index[0]
    col = index[1]
    for i in range(len(grid)):
        if (grid[row][i] in possible_vals):
            possible_vals.remove(grid[row][i])
        if (grid[i][col] in possible_vals):
            possible_vals.remove(grid[i][col])
    possible_vals = find_search_area_possible_values(grid, index, possible_vals)
    return(possible_vals)

def find_possible_values_row(grid,index):
    row = index[0]
    not_possible_vals = []
    for i in range(0, len(grid)):
        if (grid[row][i] != 0):
            not_possible_vals.append(grid[row][i])
    return(not_possible_vals)
            

# def intersection(list1, list2):
#     return list(set(list1) & set(list2))

# def possible_values_for_index(grid, index):
#     possible_vals = intersection(find_search_area_possible_values(grid,index),intersection(search_row_possible_values(grid,index),search_col_possible_values(grid,index)))
#     if(len(possible_vals) != 1):
#         possible_vals = [0]
#     return possible_vals

def solve_sudoku(grid):
    #while(is_solved(grid) == False):
    while(is_solved(grid) != True):
        unknowns = get_unknowns(grid)
        for index in unknowns:
            possible_vals = find_possible_values(grid, index)
            print(index, possible_vals)
            if (len(possible_vals) != 0):
                grid[index[0]][index[1]] = possible_vals[0]
            unknowns = get_unknowns(grid)
    print(grid)



test_grid =[
    [7,0,0,1,3,4,8,9,0],
    [8,1,4,6,9,0,0,0,3],
    [0,3,9,8,5,0,0,0,0],
    [1,9,0,5,0,3,6,0,7],
    [0,4,0,7,0,9,0,3,0],
    [0,7,3,2,0,8,0,0,9],
    [9,0,1,4,7,0,3,2,0],
    [4,2,6,3,8,1,9,7,5],
    [3,0,7,9,2,0,0,0,4]
]

#print(intersection(search_col_possible_values(test_grid,[2,0]),#search_row_possible_values(test_grid,[8,1])))
solve_sudoku(test_grid)

# index = [8,7]
# possible_vals = find_possible_values_row(test_grid, index)
# print(index,possible_vals)
# print(search_col_possible_values(test_grid, [4,0]))

# for i in range(len(test_grid)):
#     for j in range(len(test_grid)):
#         if(test_grid[i][j] == 0):
#             index = []
#             index.append(i)
#             index.append(j)
#             possible_vals = possible_values_for_index(test_grid, index)
#             print(index, possible_vals)
