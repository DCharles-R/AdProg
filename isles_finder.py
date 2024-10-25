import numpy as np

test_matrix = np.matrix("0 1 1 0 0 0 1 0 1 0; "
                        "0 1 1 0 0 0 1 1 1 0; "
                        "1 0 0 0 1 1 0 0 0 1; "
                        "0 1 0 1 1 1 0 0 0 0; "
                        "0 0 1 1 0 0 0 1 1 0")

coor_array = []
ord_array = []
pattern = 0
Rows, Columns = np.shape(test_matrix)

[[coor_array.append([i, j]) for j in range(Columns) if test_matrix[i,j] == 1] for i in range(Rows)]

def finder():
    count = 0
    global pattern
    if not ord_array:
        ord_array.append(coor_array[0])
    for index in coor_array:
        if dir_check(index):
            count += 1
        if pattern == 0 and index not in ord_array:
            ord_array.append(index)
            count += 1
        pattern = 0
    print(f"Number of islands is: {count}")

def dir_check(index):
    global pattern
    left_coor = [index[0], index[1] - 1]
    right_coor = [index[0], index[1] + 1]
    down_coor = [index[0] + 1, index[1]]
    upper_coor = [index[0] - 1, index[1]]
    if left_coor in coor_array and left_coor not in ord_array:
        ord_array.append(left_coor)
        dir_check(left_coor)
        pattern += 1
    if down_coor in coor_array and down_coor not in ord_array:
        ord_array.append(down_coor)
        dir_check(down_coor)
        pattern += 1
    if right_coor in coor_array and right_coor not in ord_array:
        ord_array.append(right_coor)
        dir_check(right_coor)
        pattern += 1
    if upper_coor in coor_array and upper_coor not in ord_array:
        ord_array.append(upper_coor)
        dir_check(upper_coor)
        pattern += 1
    if pattern != 0:
        return True

finder()
