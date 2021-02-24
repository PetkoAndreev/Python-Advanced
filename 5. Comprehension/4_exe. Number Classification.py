numbers = [int(s) for s in input().split(', ')]


def get_positive_numbers(numbers):
    return [str(s) for s in numbers if s >= 0]


def get_negative_numbers(numbers):
    return [str(s) for s in numbers if s < 0]


def get_odd_numbers(numbers):
    return [str(s) for s in numbers if s % 2 != 0]


def get_even_numbers(numbers):
    return [str(s) for s in numbers if s % 2 == 0]


def print_result(positive_numbers, negative_numbers, odd_numbers, even_numbers):
    print(f'Positive: {", ".join(positive_numbers)}')
    print(f'Negative: {", ".join(negative_numbers)}')
    print(f'Even: {", ".join(even_numbers)}')
    print(f'Odd: {", ".join(odd_numbers)}')


positive_numbers = get_positive_numbers(numbers)
negative_numbers = get_negative_numbers(numbers)
odd_numbers = get_odd_numbers(numbers)
even_numbers = get_even_numbers(numbers)
print_result(positive_numbers, negative_numbers, odd_numbers, even_numbers)