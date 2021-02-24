def read_matrix(is_tet=False):
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = [int(s) for s in input().split()]
        matrix.append(row)
    return matrix


def get_submatrix_sum(matrix, row_index, column_index, subsize):
    sub_sum = 0
    for r in range(row_index, row_index + subsize):
        for c in range(column_index, column_index + subsize):
            sub_sum += matrix[r][c]
    return sub_sum


def get_best_submatrix_coordinates(matrix, subsize):
    best_row_index = 0
    best_col_index = 0
    best_sum = get_submatrix_sum(matrix, 0, 0, subsize)

    for row_index in range(len(matrix) - subsize + 1):
        for col_index in range(len(matrix[row_index]) - subsize + 1):
            current_sum = get_submatrix_sum(matrix, row_index, col_index, subsize)
            if current_sum > best_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_col_index = col_index
    return (best_row_index, best_col_index)


def print_result(coordinates):
    (row_index, col_index) = coordinates
    print(f'Sum = {get_submatrix_sum(matrix, row_index, col_index, subsize)}')
    for r in range(row_index, row_index + subsize):
        row = []
        for c in range(col_index, col_index + subsize):
            row.append(matrix[r][c])
        print(' '.join(str(s) for s in row))


subsize = 3
matrix = read_matrix()
coordinates = get_best_submatrix_coordinates(matrix, subsize)
print_result(coordinates)