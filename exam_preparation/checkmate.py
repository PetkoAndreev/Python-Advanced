def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = [s for s in input().split()]
        matrix.append(row)
    return matrix


def get_queens_positions(size, matrix):
    queens = []
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'Q':
                coordinates = [r, c]
                queens.append(coordinates)
    return queens


def is_valid_coordinates(value, max_value):
    return 0 <= value < max_value


def queen_horizontal_moves(size, matrix, queen_row, queen_col):
    # Left horizontal moves
    left_queen_col = queen_col - 1
    while is_valid_coordinates(left_queen_col, size):
        if matrix[queen_row][left_queen_col] == 'Q':
            break
        elif matrix[queen_row][left_queen_col] == 'K':
            return True
        left_queen_col -= 1

    # Right horizontal moves
    right_queen_col = queen_col + 1
    while is_valid_coordinates(right_queen_col, size):
        if matrix[queen_row][right_queen_col] == 'Q':
            break
        elif matrix[queen_row][right_queen_col] == 'K':
            return True
        right_queen_col += 1
    # If to the left and to the right of the matrix are only '.'
    return False


def queen_vertical_moves(size, matrix, queen_row, queen_col):
    # Up vertical moves
    up_queen_row = queen_row - 1
    while is_valid_coordinates(up_queen_row, size):
        if matrix[up_queen_row][queen_col] == 'Q':
            break
        elif matrix[up_queen_row][queen_col] == 'K':
            return True
        up_queen_row -= 1

    # Down vertical moves
    down_queen_row = queen_row + 1
    while is_valid_coordinates(down_queen_row, size):
        if matrix[down_queen_row][queen_col] == 'Q':
            break
        elif matrix[down_queen_row][queen_col] == 'K':
            return True
        down_queen_row += 1
    # If to the top and to the bottom of the matrix are only '.'
    return False


def queen_diagonal_moves(size, matrix, queen_row, queen_col):
    # Left-Up diagonal moves
    up_queen_row = queen_row - 1
    left_queen_col = queen_col - 1
    while is_valid_coordinates(up_queen_row, size) and is_valid_coordinates(left_queen_col, size):
        if matrix[up_queen_row][left_queen_col] == 'Q':
            break
        elif matrix[up_queen_row][left_queen_col] == 'K':
            return True
        up_queen_row -= 1
        left_queen_col -= 1

    # Left-Down diagonal moves
    down_queen_row = queen_row + 1
    left_queen_col = queen_col - 1
    while is_valid_coordinates(down_queen_row, size) and is_valid_coordinates(left_queen_col, size):
        if matrix[down_queen_row][left_queen_col] == 'Q':
            break
        elif matrix[down_queen_row][left_queen_col] == 'K':
            return True
        down_queen_row += 1
        left_queen_col -= 1

    # Right-Up diagonal moves
    up_queen_row = queen_row - 1
    right_queen_col = queen_col + 1
    while is_valid_coordinates(up_queen_row, size) and is_valid_coordinates(right_queen_col, size):
        if matrix[up_queen_row][right_queen_col] == 'Q':
            break
        elif matrix[up_queen_row][right_queen_col] == 'K':
            return True
        up_queen_row -= 1
        right_queen_col += 1

    # Right-Down diagonal moves
    down_queen_row = queen_row + 1
    right_queen_col = queen_col + 1
    while is_valid_coordinates(down_queen_row, size) and is_valid_coordinates(right_queen_col, size):
        if matrix[down_queen_row][right_queen_col] == 'Q':
            break
        elif matrix[down_queen_row][right_queen_col] == 'K':
            return True
        down_queen_row += 1
        right_queen_col += 1
    # If to the top and to the bottom of the matrix are only '.'
    return False


def check_queens_king_capture(size, matrix, queens):
    queens_capture_the_king = []
    for queen in queens:
        queen_row = queen[0]
        queen_col = queen[1]
        if queen_horizontal_moves(size, matrix, queen_row, queen_col) or queen_vertical_moves(size, matrix, queen_row,
                                                                                              queen_col) or queen_diagonal_moves(
            size, matrix, queen_row, queen_col):
            queens_capture_the_king.append(queen)
    return queens_capture_the_king


def print_result(queens_capture_the_king):
    if queens_capture_the_king == []:
        print('The king is safe!')
    else:
        for queen in queens_capture_the_king:
            print(queen)

size = 8
matrix = read_matrix(size)
queens = get_queens_positions(size, matrix)
queens_capture_the_king = check_queens_king_capture(size, matrix, queens)
print_result(queens_capture_the_king)
