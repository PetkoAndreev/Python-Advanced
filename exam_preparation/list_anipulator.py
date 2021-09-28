from collections import deque


def add_elements(parameters, num_list):
    if parameters[1] == 'beginning':
        for num in range(len(parameters) - 1, 1, -1):
            num_list.appendleft(parameters[num])
    elif parameters[1] == 'end':
        for num in range(2, len(parameters)):
            num_list.append(parameters[num])
    return num_list


def remove_elements(parameters, num_list):
    if len(parameters) > 2:
        for i in range(int(parameters[2])):
            if parameters[1] == 'beginning':
                num_list.popleft()
            elif parameters[1] == 'end':
                num_list.pop()
    else:
        if parameters[1] == 'beginning':
            num_list.popleft()
        elif parameters[1] == 'end':
            num_list.pop()
    return num_list


def list_manipulator(num_list, *args):
    num_list = deque(num_list)
    parameters = [el for el in args]
    if parameters[0] == 'add':
        num_list = add_elements(parameters, num_list)
    elif parameters[0] == 'remove':
        num_list = remove_elements(parameters, num_list)
    num_list = [el for el in num_list]
    return num_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
