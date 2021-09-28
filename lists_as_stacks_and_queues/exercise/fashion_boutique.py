cloths_box = [int(s) for s in input().split()]
rack_capacity = int(input())
current_rack = []
racks = 0

while cloths_box:
    cloth = cloths_box[-1]
    if sum(current_rack) + cloth < rack_capacity:
        current_rack.append(cloth)
        cloths_box.pop()
        if len(cloths_box) == 0:
            racks += 1
    elif sum(current_rack) + cloth == rack_capacity and len(cloths_box) > 0:
        current_rack = []
        racks += 1
        cloths_box.pop()
    elif sum(current_rack) + cloth > rack_capacity:
        current_rack = []
        racks += 1

print(racks)