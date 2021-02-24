def read_matrix(is_tet=False):
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = [s for s in input().split()]
        matrix.append(row)
    return matrix


def command_check(matrix, data):
    if data[0] != 'swap':
        check = False
    elif len(data) != 5:
        check = False
    elif len(data) == 5:
        row_1 = int(data[1])
        col_1 = int(data[2])
        row_2 = int(data[3])
        col_2 = int(data[4])
        if row_1 not in range(len(matrix)) or row_2 not in range(len(matrix)):
            check = False
        elif col_1 not in range(len(matrix[0])) or col_2 not in range(len(matrix[0])):
            check = False
        else:
            check = True
    else:
        check = False
    return check


def get_matrix_shuffle(matrix):
    command = input()
    while command != 'END':
        data = command.split()
        # check = False
        if command_check(matrix, data):
            row_1 = int(data[1])
            col_1 = int(data[2])
            row_2 = int(data[3])
            col_2 = int(data[4])
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            print_result(matrix)
        else:
            print('Invalid input!')
        command = input()
    return matrix


def print_result(matrix):
    for r in range(len(matrix)):
        print(' '.join(s for s in matrix[r]))


matrix = read_matrix()
result = get_matrix_shuffle(matrix)