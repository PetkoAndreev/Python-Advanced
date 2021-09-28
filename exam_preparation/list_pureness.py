from collections import deque


def best_list_pureness(numbers, rotations):
    numbers = deque(numbers)
    rotations = int(rotations)
    pureness = 0
    for rotation in range(rotations + 1):
        current_pureness = 0
        for i in range(len(numbers)):
            current_pureness += i * numbers[i]
        numbers.appendleft(numbers.pop())
        if current_pureness > pureness:
            pureness = current_pureness
            pure_rotations = rotation
    return f'Best pureness {pureness} after {pure_rotations} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
