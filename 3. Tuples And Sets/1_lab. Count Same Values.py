input_data = list(map(float, input().split()))


def count_numbers(input_data):
    numbers = {}
    for el in input_data:
        if el not in numbers:
            numbers[el] = 0
        numbers[el] += 1
    return numbers


def print_data(numbers):
    for num, count in numbers.items():
        print(f'{num} - {count} times')

numbers = count_numbers(input_data)
print_data(numbers)