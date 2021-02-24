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
            row = [int(s) for s in input().split(', ')]
            matrix.append(row)
        return matrix

matrix = read_matrix()
sum_matrix = 0
for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        sum_matrix += matrix[r][c]

print(sum_matrix)
print(matrix)