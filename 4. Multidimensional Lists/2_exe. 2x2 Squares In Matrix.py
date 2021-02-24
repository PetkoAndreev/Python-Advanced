def read_matrix(is_tet=False):
    if is_tet:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        rows_count, olumns_count = map(int, input().split())
        matrix = []
        for row_index in range(rows_count):
            row = [s for s in input().split()]
            matrix.append(row)
        return matrix


def get_submatrix(matrix, row_index, col_index, subsize):
    sub_sum = 0
    for r in range(row_index, row_index + subsize):
        for c in range(col_index, col_index + subsize):
            if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
                sub_sum = 4
                break
            else:
                sub_sum = 1
                break
        if sub_sum != 0:
            break
    return sub_sum


def get_submatrix_equals(matrix, subsize):
    counter = 0

    for row_index in range(len(matrix) - subsize + 1):
        for col_index in range(len(matrix[row_index]) - subsize + 1):
            current_sum = get_submatrix(matrix, row_index, col_index, subsize)
            if current_sum == 4:
                counter += 1
    return counter


subsize = 2
matrix = read_matrix()
result = get_submatrix_equals(matrix, subsize)
print(result)