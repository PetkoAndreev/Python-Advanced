def strs_to_ints(strs):
    return [int(s) for s in strs]


def read_matrix():
    rows_counts = int(input())
    return [strs_to_ints(input().split(', ')) for _ in range(rows_counts)]


def get_flatten(matrix):
    return [s for row in matrix for s in row]


def print_result(values):
    print([s for s in values])


matrix = read_matrix()
flat = get_flatten(matrix)
print_result(flat)