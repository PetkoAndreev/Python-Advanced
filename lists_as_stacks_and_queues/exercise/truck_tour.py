from collections import deque
pumps = int(input())
petrol = deque([])
distance = deque([])
tank = 0
curr_index = 0
next_pump = 0
for pump in range(0, pumps):
    fuel, km = input().split()
    fuel = int(fuel)
    km = int(km)
    petrol.append(fuel)
    distance.append(km)

petrol.append(petrol[0])
distance.append(distance[0])

while True:
    add_to_tank = petrol[next_pump] - distance[next_pump]
    if tank + add_to_tank < 0:
        curr_index += 1
        next_pump = 0
        tank = 0
        petrol.popleft()
        petrol.append(petrol[0])
        distance.popleft()
        distance.append(distance[0])
        continue
    else:
        tank += add_to_tank
        next_pump += 1
        if next_pump == pumps:
            break

print(curr_index)