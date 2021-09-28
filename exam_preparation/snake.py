def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = [s for s in input()]
        matrix.append(row)
    return matrix


def get_snake_position(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'S':
                snake_pos = (r, c)
    return snake_pos


def get_lairs_positions(matrix, size):
    lairs = []
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                coordinates = (r, c)
                lairs.append(coordinates)
    return lairs


def is_valid_coordinates(value, max_value):
    return 0 <= value < max_value


def check_move(matrix, current_row, current_col, food_eaten, lairs):
    if matrix[current_row][current_col] == '*':
        food_eaten += 1
        matrix[current_row][current_col] = 'S'
    elif matrix[current_row][current_col] == '-':
        matrix[current_row][current_col] = 'S'
    elif matrix[current_row][current_col] == 'B':
        matrix[current_row][current_col] = '.'
        # Change second 'B' value with '.'
        for lair in lairs:
            lair_row = lair[0]
            lair_col = lair[1]
            if lair_row != current_row and lair_col != current_col:
                current_row_new = lair_row
                current_col_new = lair_col
        current_row = current_row_new
        current_col = current_col_new
        matrix[current_row][current_col] = 'S'
    return current_row, current_col, matrix, food_eaten


def get_snake_moves(size, matrix, snake_pos, lairs):
    current_row = snake_pos[0]
    current_col = snake_pos[1]
    food_eaten = 0
    matrix[current_row][current_col] = '.'
    game_over = False
    while True:
        move = input()
        if move == '':
            break
        matrix[current_row][current_col] = '.'
        if move == 'left':
            current_col -= 1
            if is_valid_coordinates(current_col, size):
                current_row, current_col, matrix, food_eaten = check_move(matrix, current_row, current_col, food_eaten,
                                                                          lairs)
            else:
                game_over = True
        elif move == 'right':
            current_col += 1
            if is_valid_coordinates(current_col, size):
                current_row, current_col, matrix, food_eaten = check_move(matrix, current_row, current_col, food_eaten,
                                                                          lairs)
            else:
                game_over = True
        elif move == 'up':
            current_row -= 1
            if is_valid_coordinates(current_row, size):
                current_row, current_col, matrix, food_eaten = check_move(matrix, current_row, current_col, food_eaten,
                                                                          lairs)
            else:
                game_over = True
        elif move == 'down':
            current_row += 1
            if is_valid_coordinates(current_row, size):
                current_row, current_col, matrix, food_eaten = check_move(matrix, current_row, current_col, food_eaten,
                                                                          lairs)
            else:
                game_over = True
        if game_over or food_eaten == 10:
            break
    return matrix, game_over, food_eaten


def print_result(matrix, game_over, food_eaten):
    if game_over:
        print('Game over!')
    else:
        print('You won! You fed the snake.')
    print(f'Food eaten: {food_eaten}')
    for r in range(size):
        print(''.join(s for s in matrix[r]))


size = int(input())
matrix = read_matrix(size)
snake_pos = get_snake_position(matrix, size)
lairs = get_lairs_positions(matrix, size)
matrix, game_over, food_eaten = get_snake_moves(size, matrix, snake_pos, lairs)
print_result(matrix, game_over, food_eaten)
