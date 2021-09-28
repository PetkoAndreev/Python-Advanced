def read_matrix():
    size = int(input())
    return [[int(s) for s in (input().split(', '))] for _ in range(size)]


def get_primary_diagonal(matrix):
    size = len(matrix)
    primary_diagonal = []
    for r in range(size):
        for c in range(size):
            if r == c:
                primary_diagonal.append(matrix[r][c])
    return primary_diagonal


def get_secondary_diagonal(matrix):
    size = len(matrix)
    secondary_diagonal = []
    for r in range(size):
        secondary_diagonal.append(matrix[r][size - r - 1])
    return secondary_diagonal


def print_result(primary_diagonal, secondary_diagonal):
    print(f'First diagonal: {", ".join([str(s) for s in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
    print(f'Second diagonal: {", ".join([str(s) for s in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')


matrix = read_matrix()
primary_diagonal = get_primary_diagonal(matrix)
secondary_diagonal = get_secondary_diagonal(matrix)
print_result(primary_diagonal, secondary_diagonal)