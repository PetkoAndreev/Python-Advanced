num = int(input())
names = set()

def input_lines(number):
    lines = set()
    for _ in range(number):
        lines.add(input())

    return lines

names = input_lines(num)

for name in names:
    print(name)