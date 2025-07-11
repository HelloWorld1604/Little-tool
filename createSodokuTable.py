import numpy as np
import random

# take a random number
def get_the_random_number():
    while(True):
        index = random.randint(0,8)
        if numbers[index] != 0:
            num = numbers[index]
            numbers[index] = 0
            break
    
    return num

# clear every chances of n can be filled in 4 directions
def clear_zero(i, j):
    table[0:,j][table[0:,j]==0] = 100 #column
    table[i,0:][table[i,0:]==0] = 100 #line

# count how many 0 in the grid
def count(pos):
    # pos[0]: first start point of column: x
    # pos[1]: first start point of line: y
    return np.count_nonzero(table[pos[0]:(pos[0]+3),pos[1]:(pos[1]+3)] == 0)


# find the grid that include the least number 0
def find_min_grid():
    min = 9
    pos_x = 0
    pos_y = 0
    for grid_pos in grids:
        cnt = count(grid_pos)
        if cnt <= min and cnt != 0:
            min = cnt
            pos_x = grid_pos[0]
            pos_y = grid_pos[1]

    return [pos_x,pos_y]

def fill_grids(num):
    done = 1
    while (done != 9):
        #print(table)
        # Find the grid that include the least 0
        coor = find_min_grid()

        #Fill n into the grid that include the least 0
        for coor_x in range(coor[0],coor[0]+3):
            # when not filled n yet
            stop_check = False
            for coor_y in range(coor[1], coor[1]+3):
                if table[coor_x][coor_y] == 0:
                    table[coor_x][coor_y] = num
                    # fill 100 in the 0 in 3x3 size
                    table[coor[0]:(coor[0]+3),coor[1]:(coor[1]+3)][table[coor[0]:(coor[0]+3),coor[1]:(coor[1]+3)]==0] = 100
                    # fill 100 in the 0 in 4 directions
                    clear_zero(coor_x,coor_y)
                    done += 1
                    stop_check = True
                    break
            
            # when have filled n in the table, then stop
            if stop_check == True:
                break


# setting sodoku's table
# table's size: 9x9
# where 0 are that numbers can be filled
table = np.array([
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0]
])

# save the number have been choosen
numbers = [1,2,3,4,5,6,7,8,9]
# save other 8 grids's size || start index [x, y]
grids = [[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]

for x in range(0,3):
    for y in range(0,3):
        n = get_the_random_number()
        table[x][y] = n
        
        # clear every 0 in the 3x3 current array
        table[:3,:3][table[:3,:3] == 0] = 100
        clear_zero(x, y)

        # Fill n into other grids 
        fill_grids(n)

        # reset table to check another number
        table[table==100] = 0

print(table)
