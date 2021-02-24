input_data = input().split(', ')


def get_words_lengths(words):
    return [f'{s} -> {len(s)}' for s in words]


def print_result(words):
    print(', '.join(words))


words = get_words_lengths(input_data)
print_result(words)