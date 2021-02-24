def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = [s for s in input()]
        matrix.append(row)
    return matrix


def get_knight_positions(size, matrix):
    knights = []
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'K':
                coordinates = (r, c)
                knights.append(coordinates)
    return knights


def get_knights_fights(size, matrix, knights):
    max_knight_fights = 0
    for i in range(len(knights)):
        current_knight_fights = 0
        knight_row = knights[i][0]
        knight_column = knights[i][1]
        knight_left_horizontal_up = (knight_row - 1, knight_column - 2)
        knight_left_horizontal_down = (knight_row + 1, knight_column - 2)
        knight_right_horizontal_up = (knight_row - 1, knight_column + 2)
        knight_right_horizontal_down = (knight_row + 1, knight_column + 2)
        knight_up_vertical_left = (knight_row - 2, knight_column - 1)
        knight_down_vertical_left = (knight_row + 2, knight_column - 1)
        knight_up_vertical_right = (knight_row - 2, knight_column + 1)
        knight_down_vertical_right = (knight_row + 2, knight_column + 1)
        # Check current knight fights
        # Left horizontal up
        if knight_left_horizontal_up[0] in range(size) and knight_left_horizontal_up[1] in range(size):
            r = knight_left_horizontal_up[0]
            c = knight_left_horizontal_up[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Left horizontal down
        if knight_left_horizontal_down[0] in range(size) and knight_left_horizontal_down[1] in range(size):
            r = knight_left_horizontal_down[0]
            c = knight_left_horizontal_down[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Right horizontal up
        if knight_right_horizontal_up[0] in range(size) and knight_right_horizontal_up[1] in range(size):
            r = knight_right_horizontal_up[0]
            c = knight_right_horizontal_up[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Right horizontal down
        if knight_right_horizontal_down[0] in range(size) and knight_right_horizontal_down[1] in range(size):
            r = knight_right_horizontal_down[0]
            c = knight_right_horizontal_down[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Up vertical left
        if knight_up_vertical_left[0] in range(size) and knight_up_vertical_left[1] in range(size):
            r = knight_up_vertical_left[0]
            c = knight_up_vertical_left[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Down vertical left
        if knight_down_vertical_left[0] in range(size) and knight_down_vertical_left[1] in range(size):
            r = knight_down_vertical_left[0]
            c = knight_down_vertical_left[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Up vertical right
        if knight_up_vertical_right[0] in range(size) and knight_up_vertical_right[1] in range(size):
            r = knight_up_vertical_right[0]
            c = knight_up_vertical_right[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Down vertical right
        if knight_down_vertical_right[0] in range(size) and knight_down_vertical_right[1] in range(size):
            r = knight_down_vertical_right[0]
            c = knight_down_vertical_right[1]
            if matrix[r][c] == 'K':
                current_knight_fights += 1
        # Check biggest fights
        if current_knight_fights > max_knight_fights:
            max_knight_fights = current_knight_fights
            knight_coordinates = knights[i]
        if max_knight_fights == 0:
            knight_coordinates = (-1, -1)
    return max_knight_fights, knight_coordinates


def remove_knight_fighters(size, matrix, knight_coordinates):
    knight_row = knight_coordinates[0]
    knight_column = knight_coordinates[1]
    is_removed = False
    if knight_row in range(size) and knight_column in range(size):
        for r in range(size):
            for c in range(size):
                if r == knight_row and c == knight_column:
                    matrix[r][c] = '0'
                    is_removed = True
                    break
            if is_removed:
                break
    return matrix


size = int(input())
matrix = read_matrix(size)
knight_fights = 0
removed_knights = 0
while True:
    knights = get_knight_positions(size, matrix)
    knight_fights, knight_coordinates = get_knights_fights(size, matrix, knights)
    if knight_fights > 0:
        matrix = remove_knight_fighters(size, matrix, knight_coordinates)
        removed_knights += 1
    else:
        break
print(removed_knights)