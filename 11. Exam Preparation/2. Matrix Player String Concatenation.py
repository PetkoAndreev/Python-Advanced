def read_matrix(sie):
    matrix = []
    for row_index in range(size):
        row = [s for s in input()]
        matrix.append(row)
    return matrix


def find_player(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'P':
                return (r, c)


def is_valid_coordinates(value, max_value):
    return 0 <= value < max_value


def change_new_coordinates(matrix, player_row, player_col, result_str):
    if matrix[player_row][player_col] != '-':
        result_str += matrix[player_row][player_col]
    matrix[player_row][player_col] = 'P'
    return matrix, result_str


def player_moves(matrix, player_coordinates, result_str):
    player_row = int(player_coordinates[0])
    player_col = int(player_coordinates[1])
    num_commands = int(input())
    for i in range(num_commands):
        command = input()
        if command == 'up':
            if is_valid_coordinates(player_row - 1, len(matrix)):
                matrix[player_row][player_col] = '-'
                player_row -= 1
                matrix, result_str = change_new_coordinates(matrix, player_row, player_col, result_str)
            else:
                if len(result_str) > 0:
                    result_str = result_str[:-1]

        elif command == 'down':
            if is_valid_coordinates(player_row + 1, len(matrix)):
                matrix[player_row][player_col] = '-'
                player_row += 1
                matrix, result_str = change_new_coordinates(matrix, player_row, player_col, result_str)
            else:
                if len(result_str) > 0:
                    result_str = result_str[:-1]

        elif command == 'left':
            if is_valid_coordinates(player_col - 1, len(matrix)):
                matrix[player_row][player_col] = '-'
                player_col -= 1
                matrix, result_str = change_new_coordinates(matrix, player_row, player_col, result_str)
            else:
                if len(result_str) > 0:
                    result_str = result_str[:-1]

        elif command == 'right':
            if is_valid_coordinates(player_col + 1, len(matrix)):
                matrix[player_row][player_col] = '-'
                player_col += 1
                matrix, result_str = change_new_coordinates(matrix, player_row, player_col, result_str)
            else:
                if len(result_str) > 0:
                    result_str = result_str[:-1]

    return result_str, matrix


def print_result(result_str, matrix):
    print(result_str)
    for r in range(len(matrix)):
        print(''.join(s for s in matrix[r]))


result_str = input()
size = int(input())
matrix = read_matrix(size)
player_coordinates = find_player(matrix)
result_str, matrix = player_moves(matrix, player_coordinates, result_str)
print_result(result_str, matrix)
