from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))
water_waste = 0

while len(bottles) > 0:
    if cups:
        current_bottle = bottles.pop()
        if current_bottle >= cups[0]:
            water_waste += current_bottle - cups.popleft()
        else:
            cups[0] -= current_bottle
    else:
        break

if len(bottles) == 0:
    print(f'Cups: {" ".join([str(s) for s in cups])}')
else:
    print(f'Bottles: {" ".join([str(s) for s in bottles])}')
print(f'Wasted litters of water: {water_waste}')