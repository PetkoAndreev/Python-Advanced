from collections import deque

dispencer_quantity = int(input())


def input_names():
    command = input()
    people = deque([])
    while command != 'Start':
        people.append(command)
        command = input()
    return people


def input_commands(people, dispencer_quantity):
    input_command = input()
    while input_command != 'End':
        if 'refill' in input_command:
            command, liters = input_command.split()
            dispencer_quantity += int(liters)
        else:
            if dispencer_quantity - int(input_command) >= 0:
                dispencer_quantity -= int(input_command)
                print(f'{people.popleft()} got water')
            else:
                print(f'{people.popleft()} must wait')
        input_command = input()
    print(f'{dispencer_quantity} liters left')


people = input_names()
input_commands(people, dispencer_quantity)