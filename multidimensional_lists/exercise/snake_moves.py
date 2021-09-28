from collections import deque


def read_matrix(is_tet=False):
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = []
        for c in range(columns_count):
            row.append('a')
        matrix.append(row)
    return matrix


def get_snake_moves(matrix):
    data = input()
    snake = deque([])
    for ch in data:
        snake.append(ch)
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for r in range(rows_count):
        row = deque([])
        for c in range(columns_count):
            current_move = snake.popleft()
            snake.append(current_move)
            if r % 2 == 0:
                row.append(current_move)
            else:
                row.appendleft(current_move)
        print(''.join(str(s) for s in row))


matrix = read_matrix()
result = get_snake_moves(matrix)