def read_matrix(is_tet=False):
    if is_tet:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        (rows_count, columns_count) = map(int, input().split(', '))
        matrix = []
        for row_index in range(rows_count):
            row = [int(s) for s in input().split()]
            matrix.append(row)
        return matrix


def get_sum_matrix_columns(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    sum_matrix_columns = [0] * columns_count
    for r in range(rows_count):
        for c in range(columns_count):
            sum_matrix_columns[c] += matrix[r][c]
    return sum_matrix_columns


def print_result(values):
    [print(s) for s in values]


matrix = read_matrix()
result = get_sum_matrix_columns(matrix)
print_result(result)