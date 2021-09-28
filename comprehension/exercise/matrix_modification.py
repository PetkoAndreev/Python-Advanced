def read_matrix():
    size = int(input())
    return [[int(s) for s in (input().split(' '))] for _ in range(size)]

def get_add_command(matrix, row, col, value):
    if row in range(len(matrix)) and col in range(len(matrix)):
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if r == row and c == col:
                    matrix[r][c] += value
    else:
        print('Invalid coordinates')
    return matrix



def get_subtract_command(matrix, row, col, value):
    if row in range(len(matrix)) and col in range(len(matrix)):
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if r == row and c == col:
                    matrix[r][c] -= value
    else:
        print('Invalid coordinates')
    return matrix


def get_loop_through_matrix(matrix):
    data = input()
    while data != 'END':
        command, row, col, value = data.split()
        row = int(row)
        col = int(col)
        value = int(value)
        if command == 'Add':
            get_add_command(matrix, row, col, value)
        elif command == 'Subtract':
            get_subtract_command(matrix, row, col, value)
        data = input()


def print_result(matrix):
    for r in range(len(matrix)):
        print(' '.join([str(s) for s in matrix[r]]))


matrix = read_matrix()
result = get_loop_through_matrix(matrix)
print_result(matrix)