start = int(input())
end = int(input())


def is_divide(number):
    return any(number % i == 0 for i in range(2, 11))


def get_divise_numbers(start, end):
    return [s for s in range(start, end + 1) if is_divide(s)]


def print_result(numbers):
    print(numbers)


numbers = get_divise_numbers(start, end)
print_result(numbers)