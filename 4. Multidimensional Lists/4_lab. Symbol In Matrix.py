def read_matrix(is_tet=False):
    if is_tet:
        return [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['X', '!', '@'],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [s for s in input()]
            matrix.append(row)
        return matrix


def find_symbol(matrix, symbol):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for r in range(rows_count):
        if symbol in matrix[r]:
            return (r, matrix[r].index(symbol))


def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_matrix()
symbol = input()
result = find_symbol(matrix, symbol)
print_result(result, symbol)