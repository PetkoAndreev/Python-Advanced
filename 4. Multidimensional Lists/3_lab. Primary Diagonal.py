def read_matrix(is_tet=False):
    if is_tet:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [int(s) for s in input().split()]
            matrix.append(row)
        return matrix


def get_primary_diagonal_sum(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    sum_matrix_primary_diagonal = 0
    for r in range(rows_count):
        for c in range(columns_count):
            if r == c:
                sum_matrix_primary_diagonal += matrix[r][c]
    return sum_matrix_primary_diagonal


matrix = read_matrix()
result = get_primary_diagonal_sum(matrix)
print(result)