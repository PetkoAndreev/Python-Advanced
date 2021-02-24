def read_matrix(is_tet=False):
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [int(s) for s in input().split()]
        matrix.append(row)
    return matrix

def get_bombs(matrix):
    bombs = input().split()
    bombs_coordinates = []
    for bomb in bombs:
        bomb_row, bomb_column = [int(s) for s in bomb.split(',')]
        bombs_coordinates.append(bomb_row)
        bombs_coordinates.append(bomb_column)
    return bombs_coordinates


def get_bombs_explodes(matrix, bombs):
    size = len(matrix)
    for i in range(0, len(bombs), 2):
        prev_row = bombs[i] - 1
        prev_col = bombs[i + 1] - 1

        same_row = bombs[i]
        same_col = bombs[i + 1]

        next_row = bombs[i] + 1
        next_col = bombs[i + 1] + 1

        for r in range(size):
            for c in range(size):
                if r == same_row and c == same_col:
                    if matrix[r][c] > 0:
                        bomb_damage = matrix[r][c]
                        matrix[r][c] = 0
                        # Same row left cell
                        if same_row in range(size) and prev_col in range(size):
                            if matrix[same_row][prev_col] > 0:
                                matrix[same_row][prev_col] -= bomb_damage
                        # Same row right cell
                        if same_row in range(size) and next_col in range(size):
                            if matrix[same_row][next_col] > 0:
                                matrix[same_row][next_col] -= bomb_damage
                        # Prev row topleft cell
                        if prev_row in range(size) and prev_col in range(size):
                            if matrix[prev_row][prev_col] > 0:
                                matrix[prev_row][prev_col] -= bomb_damage
                        # Prev row top cell
                        if prev_row in range(size) and same_col in range(size):
                            if matrix[prev_row][same_col] > 0:
                                matrix[prev_row][same_col] -= bomb_damage
                        # Prev row topright cell
                        if prev_row in range(size) and next_col in range(size):
                            if matrix[prev_row][next_col] > 0:
                                matrix[prev_row][next_col] -= bomb_damage
                        # Next row bottomleft cell
                        if next_row in range(size) and prev_col in range(size):
                            if matrix[next_row][prev_col] > 0:
                                matrix[next_row][prev_col] -= bomb_damage
                        # Next row bottom cell
                        if next_row in range(size) and same_col in range(size):
                            if matrix[next_row][same_col] > 0:
                                matrix[next_row][same_col] -= bomb_damage
                        # Next row bottomright cell
                        if next_row in range(size) and next_col in range(size):
                            if matrix[next_row][next_col] > 0:
                                matrix[next_row][next_col] -= bomb_damage
    return matrix
#
#
# def get_modified_matrix(matrix, bombs):
#     size = len(matrix)
#     for i in range(0, len(bombs), 3):
#         for r in range(size):
#             for c in range(size):
#                 if r == bombs[i] and c == bombs[i + 1]:
#                     matrix[r][c] = 0
#     return matrix


def print_result(matrix):
    size = len(matrix)
    alive_cells = 0
    sum_alive_cells = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] > 0:
                alive_cells += 1
                sum_alive_cells += matrix[r][c]
    print(f'Alive cells: {alive_cells}')
    print(f'Sum: {sum_alive_cells}')
    for r in range(size):
        row = []
        for c in range(size):
            row.append(matrix[r][c])
        print(' '.join(str(s) for s in row))


matrix = read_matrix()
bombs = get_bombs(matrix)
exploded_matrix = get_bombs_explodes(matrix, bombs)
# mod_matrix = get_modified_matrix(exploded_matrix, bombs)
print_result(exploded_matrix)