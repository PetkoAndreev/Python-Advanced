num = int(input())

def input_lines(number):
    lines = set()
    for _ in range(number):
        commad, car_num = input().split(', ')
        if commad == 'IN':
            lines.add(car_num)
        else:
            lines.remove(car_num)
    return lines


def print_data(cars):
    if cars:
        for car in cars:
            print(car)
    else:
        print('Parking Lot is Empty')

cars = input_lines(num)
print_data(cars)