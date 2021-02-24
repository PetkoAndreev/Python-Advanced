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


def get_secondary_diagonal_sum(matrix):
    size = len(matrix)
    sum_matrix_secondary_diagonal = 0
    for r in range(size):
        sum_matrix_secondary_diagonal += matrix[r][size - r - 1]
    return sum_matrix_secondary_diagonal


matrix = read_matrix()
primary_diagonal_sum = get_primary_diagonal_sum(matrix)
secondary_diagonal = get_secondary_diagonal_sum(matrix)
print(abs(primary_diagonal_sum - secondary_diagonal))