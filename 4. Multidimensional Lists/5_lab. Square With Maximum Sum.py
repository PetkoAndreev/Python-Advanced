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


def submatrix_sum(matrix, row_index, col_index, submatrix_size):
    sub_sum = 0
    for r in range(row_index, row_index + submatrix_size):
        for c in range(col_index, col_index + submatrix_size):
            sub_sum += matrix[r][c]
    return sub_sum


def best_submatrix_sum_coordinates(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = submatrix_sum(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = submatrix_sum(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(submatrix_sum(matrix, row_index, col_index, size))


submatrix_size = 2
matrix = read_matrix()
coordinates = best_submatrix_sum_coordinates(matrix, submatrix_size)
print_result(coordinates, submatrix_size)