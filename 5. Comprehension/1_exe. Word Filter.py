input_data = input().split()


def is_even(word):
    return len(word) % 2 == 0


def get_even_len_words(words):
    return [word for word in words if is_even(word)]


def print_result(words):
    [print(word) for word in words]


words = get_even_len_words(input_data)
print_result(words)