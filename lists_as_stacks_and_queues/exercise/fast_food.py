from collections import deque

food_quantity = int(input())
orders = input().split()
orders = [int(s) for s in orders]

q = deque(orders)

if len(q) > 0:
    print(max(q))

while q:
    order = q[0]
    if food_quantity - order >= 0:
        food_quantity -= order
        q.popleft()
    else:
        break

if len(q) == 0:
    print('Orders complete')
else:
    print(f'Orders left: ', end = '')
    while q:
        print(q.popleft(), end = ' ')