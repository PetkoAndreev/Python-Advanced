from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence_value = int(input())
bullets_cost = 0
bullets_shot = 0
# Bullets - back to front - Stack
# Locks - front to back - Queue

while len(bullets) > 0:
    if locks:
        current_bullet = bullets.pop()
        bullets_shot += 1
        bullets_cost += bullet_price
        if current_bullet <= locks[0]:
            locks.popleft()
            print('Bang!')
        else:
            print('Ping!')
        if bullets_shot == gun_barrel and len(bullets) > 0:
            bullets_shot = 0
            print('Reloading!')
    else:
        break

if len(locks) == 0:
    print(f'{len(bullets)} bullets left. Earned ${intelligence_value - bullets_cost}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')