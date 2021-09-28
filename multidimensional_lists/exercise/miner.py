def read_matrix(size):
    matrix = []
    for row_index in range(size):
        row = [s for s in input().split()]
        matrix.append(row)
    return matrix


def get_matrix_details(matrix, size):
    start_row_index = 0
    start_col_index = 0
    coals = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'c':
                coals += 1
            elif matrix[r][c] == 's':
                start_row_index = r
                start_col_index = c
    return (start_row_index, start_col_index, coals)


def get_miner_moves(matrix, size, commands, start_row_index, start_col_index, coals):
    current_row = start_row_index
    current_column = start_col_index
    for i in range(len(commands)):
        command = commands[i]
        # Up command
        if command == 'up' and current_row - 1 in range(size):
            current_row -= 1
        # Down command
        elif command == 'down' and current_row + 1 in range(size):
            current_row += 1
        # Left command
        elif command == 'left' and current_column - 1 in range(size):
            current_column -= 1
        # Right command
        elif command == 'right' and current_column + 1 in range(size):
            current_column += 1

        if matrix[current_row][current_column] == 'c':
            matrix[current_row][current_column] = '*'
            coals -= 1
            if coals == 0:
                print(f'You collected all coals! ({current_row}, {current_column})')
                break
        elif matrix[current_row][current_column] == 'e':
            print(f'Game over! ({current_row}, {current_column})')
        elif i == len(commands) - 1:
            print(f'{coals} coals left. ({current_row}, {current_column})')


size = int(input())
commands = input().split()
matrix = read_matrix(size)
start_row_index, start_col_index, coals = get_matrix_details(matrix, size)
get_miner_moves(matrix, size, commands, start_row_index, start_col_index, coals)