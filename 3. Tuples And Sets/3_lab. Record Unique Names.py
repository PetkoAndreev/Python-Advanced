num = int(input())

def input_lines(number):
    lines = set()
    for _ in range(number):
        lines.add(input())
    return lines


def print_data(names):
    for name in names:
        print(name)


names = input_lines(num)
print_data(names)