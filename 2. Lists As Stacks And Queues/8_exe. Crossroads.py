from collections import deque

green_time = int(input())
free_time = int(input())

cars = deque()
cars_passed = 0
is_crash = False

command = input()

while command != 'END':
    if command == 'green':
        if cars:
            current_car = cars.popleft()
            time_left = green_time - len(current_car)
            while time_left > 0:
                cars_passed += 1
                if cars:
                    current_car = cars.popleft()
                    time_left -= len(current_car)
                else:
                    break
            if time_left == 0:
                cars_passed += 1
            if free_time >= abs(time_left):
                if time_left < 0:
                    cars_passed += 1
            else:
                index = free_time + time_left
                print('A crash happened!')
                print(f'{current_car} was hit at {current_car[index]}.')
                is_crash = True
                break
    else:
        cars.append(command)
    command = input()

if not is_crash:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')