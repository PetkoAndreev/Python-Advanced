def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = ['' for _ in range(size)]
        matrix.append(row)
    return matrix


def is_valid_coordinates(value, max_value):
    return 0 <= value < max_value


def place_bombs(matrix, size, bombs):
    for bomb in range(bombs):
        bomb_row, bomb_col = [int(s) for s in input().replace('(', '').replace(')', '').split(', ')]
        if is_valid_coordinates(bomb_row, size) and is_valid_coordinates(bomb_col, size):
            matrix[bomb_row][bomb_col] = '*'
    return matrix


def check_for_bomb(size, row, col):
    matrix_el_value = 0
    # Left horizontal bomb
    curr_col = col - 1
    if is_valid_coordinates(curr_col, size) and matrix[row][curr_col] == '*':
        matrix_el_value += 1
    # Right horizontal bomb
    curr_col = col + 1
    if is_valid_coordinates(curr_col, size) and matrix[row][curr_col] == '*':
        matrix_el_value += 1
    # Up vertical bomb
    curr_row = row - 1
    if is_valid_coordinates(curr_row, size) and matrix[curr_row][col] == '*':
        matrix_el_value += 1
    # Down vertical bomb
    curr_row = row + 1
    if is_valid_coordinates(curr_row, size) and matrix[curr_row][col] == '*':
        matrix_el_value += 1
    # Up left diagonal bomb
    curr_row = row - 1
    curr_col = col - 1
    if is_valid_coordinates(curr_row, size) and is_valid_coordinates(curr_col, size) and matrix[curr_row][
        curr_col] == '*':
        matrix_el_value += 1
    # Down left diagonal bomb
    curr_row = row + 1
    curr_col = col - 1
    if is_valid_coordinates(curr_row, size) and is_valid_coordinates(curr_col, size) and matrix[curr_row][
        curr_col] == '*':
        matrix_el_value += 1
    # Up right diagonal bomb
    curr_row = row - 1
    curr_col = col + 1
    if is_valid_coordinates(curr_row, size) and is_valid_coordinates(curr_col, size) and matrix[curr_row][
        curr_col] == '*':
        matrix_el_value += 1
    # Down right diagonal bomb
    curr_row = row + 1
    curr_col = col + 1
    if is_valid_coordinates(curr_row, size) and is_valid_coordinates(curr_col, size) and matrix[curr_row][
        curr_col] == '*':
        matrix_el_value += 1

    return str(matrix_el_value)


def place_numbers(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == '':
                matrix[r][c] = check_for_bomb(size, r, c)
    return matrix


def print_result(matrix, size):
    for r in range(size):
        print(' '.join(s for s in matrix[r]))


size = int(input())
bombs = int(input())
matrix = read_matrix(size)
matrix = place_bombs(matrix, size, bombs)
matrix = place_numbers(matrix, size)
print_result(matrix, size)
