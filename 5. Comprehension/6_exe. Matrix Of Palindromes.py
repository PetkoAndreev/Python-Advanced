def read_matrix():
    data = input().split()
    rows = int(data[0])
    columns = int(data[1])
    return [[str(s) for s in range(columns)] for _ in range(rows)]


def get_palindrome_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    first_char_ascii = 97
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = chr(first_char_ascii) + chr(first_char_ascii + c) + chr(first_char_ascii)
        first_char_ascii += 1
    return matrix


def print_result(matrix):
    for r in range(len(matrix)):
        print(" ".join(matrix[r]))


matrix = read_matrix()
palindrome_matrix = get_palindrome_matrix(matrix)
print_result(palindrome_matrix)