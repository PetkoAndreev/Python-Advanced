from collections import deque
from _datetime import datetime, timedelta

data = input().split(';')
robots = deque([])
products = deque([])

start_time = datetime.strptime(input(), '%H:%M:%S')
time_add = timedelta(seconds=1)
product_time = start_time + time_add

robot = {}
# Adding robots as dictionary to the robots deque
for el in data:
    robot = {}
    name, time = el.split('-')
    time = int(time)
    robot['name'] = name
    robot['processing_time'] = time
    robot['available_at'] = product_time
    robots.append(robot)

product = input()
# Adding products to the products deque
while product != 'End':
    products.append(product)
    product = input()

# Looping through product line and robots to calculate processing time for each product
while len(products) > 0:
    current_product = products.popleft()
    is_not_available = True
    for current_robot in robots:
        if product_time >= current_robot['available_at']:
            current_robot['available_at'] = product_time + timedelta(seconds = current_robot['processing_time'])
            print(f'{current_robot["name"]} - {current_product} [{product_time.strftime("%H:%M:%S")}]')
            is_not_available = False
            break
    if is_not_available:
        products.append(current_product)
    product_time += time_add