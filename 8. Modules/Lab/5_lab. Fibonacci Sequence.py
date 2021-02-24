from Modules import fibonacci_sequence

command = input()

while command != 'Stop':
    if 'Create' in command:
        num = command.split()[-1]
        num = int(num)
        result = fibonacci_sequence.create_fibonacci(num)
        print(*result)
    else:
        num = command.split()[-1]
        num = int(num)
        print(fibonacci_sequence.locate_number(num))
    command = input()