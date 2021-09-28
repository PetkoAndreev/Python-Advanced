num = int(input())


def input_lines(number):
    lines = set()
    for _ in range(number):
        elements = input().split()
        for element in elements:
            lines.add(element)
    return lines


def print_data(result):
    for el in elements:
        print(el)


elements = input_lines(num)

print_data(elements)