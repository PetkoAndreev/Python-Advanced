num = int(input())

def input_lines(number):
    result = []
    for _ in range(number):
        range_1, range_2 = input().split('-')
        num_1, num_2 = map(int, range_1.split(','))
        num_3, num_4 = map(int, range_2.split(','))
        intersection_1 = set()
        intersection_2 = set()
        for num_int_1 in range(num_1, num_2 + 1):
            intersection_1.add(num_int_1)

        for num_int_2 in range(num_3, num_4 + 1):
            intersection_2.add(num_int_2)

        current_intersection = list(intersection_1.intersection(intersection_2))
        if len(current_intersection) > len(result):
            result = current_intersection

    return result


def print_data(intersection):
    print(f'Longest intersection is {intersection} with length {len(intersection)}')


intersection = input_lines(num)
print_data(intersection)