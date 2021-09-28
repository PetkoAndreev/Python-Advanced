# from collections import deque
#
#
# def get_firework_creation(firework_effects, firework_explosive_power):
#     palm_counter = 0
#     willow_counter = 0
#     crossette_counter = 0
#     is_enough_fireworks = False
#
#     while len(firework_effects) != 0 and len(firework_explosive_power) != 0:
#         if firework_effects[0] >= 0 and firework_explosive_power[-1] >= 0:
#             current_firework_value = firework_effects[0] + firework_explosive_power[-1]
#
#         else:
#             if firework_explosive_power[-1] <= 0:
#                 firework_explosive_power.pop()
#             else:
#                 firework_effects.pop()
#             continue
#         if firework_effects[0] <= 0 and firework_explosive_power[-1] <= 0:
#             firework_effects.popleft()
#             firework_explosive_power.pop()
#
#         if current_firework_value % 3 == 0 and current_firework_value % 5 == 0:
#             crossette_counter += 1
#             firework_effects.popleft()
#             firework_explosive_power.pop()
#
#         elif current_firework_value % 3 == 0:
#             palm_counter += 1
#             firework_effects.popleft()
#             firework_explosive_power.pop()
#
#         elif current_firework_value % 5 == 0:
#             willow_counter += 1
#             firework_effects.popleft()
#             firework_explosive_power.pop()
#         else:
#             firework_effects[0] -= 1
#             element = firework_effects.popleft()
#             firework_effects.append(element)
#
#         if palm_counter >= 3 and willow_counter >= 3 and crossette_counter >= 3:
#             is_enough_fireworks = True
#             break
#
#     return firework_effects, firework_explosive_power, palm_counter, willow_counter, crossette_counter, is_enough_fireworks
#
#
# def print_result(firework_effects, firework_explosive_power, palm_counter, willow_counter, crossette_counter,
#                  is_enough_fireworks):
#     if is_enough_fireworks:
#         print('Congrats! You made the perfect firework show!')
#     else:
#         print('Sorry. You can’t make the perfect firework show.')
#     if len(firework_effects) > 0:
#         print(f'Firework effects left: {", ".join(str(s) for s in firework_effects)}')
#     if len(firework_explosive_power) > 0:
#         print(f'Explosive Power left: {", ".join(str(s) for s in firework_explosive_power)}')
#     print(f'Palm Fireworks: {palm_counter}')
#     print(f'Willow Fireworks: {willow_counter}')
#     print(f'Crossette Fireworks: {crossette_counter}')
#
#
# firework_effects = deque([int(s) for s in input().split(', ') if 0 < int(s) < 101])
# firework_explosive_power = [int(s) for s in input().split(', ') if 0 < int(s) < 101]
# firework_effects, firework_explosive_power, palm_counter, willow_counter, crossette_counter, is_enough_fireworks = get_firework_creation(
#     firework_effects, firework_explosive_power)
# print_result(firework_effects, firework_explosive_power, palm_counter, willow_counter, crossette_counter,
#              is_enough_fireworks)

from collections import deque

firework_efects = deque([int(s) for s in input().split(", ") if int(s) > 0])
firework_explosive_power = [int(s) for s in input().split(", ") if int(s) > 0]

palm_counter = 0
willow_counter = 0
crossette_counter = 0
is_enough_fireworks = False

while len(firework_efects) != 0 and len(firework_explosive_power) != 0:
    if firework_efects[0] >= 0 and firework_explosive_power[-1] >= 0:
        current_value = firework_efects[0] + firework_explosive_power[-1]

    else:
        if firework_explosive_power[-1] <= 0:
            firework_explosive_power.pop()
        else:
            firework_efects.pop()
        continue
    if firework_efects[0] <= 0 and firework_explosive_power[-1] <= 0:
        firework_efects.popleft()
        firework_explosive_power.pop()

    if current_value % 3 == 0 and current_value % 5 == 0:
        crossette_counter += 1
        firework_efects.popleft()
        firework_explosive_power.pop()

    elif current_value % 3 == 0:
        palm_counter += 1
        firework_efects.popleft()
        firework_explosive_power.pop()

    elif current_value % 5 == 0:
        willow_counter += 1
        firework_efects.popleft()
        firework_explosive_power.pop()

    else:
        firework_efects[0] -= 1
        firework_efects.append(firework_efects.popleft())

    if crossette_counter >= 3 and palm_counter >= 3 and willow_counter >= 3:
        is_enough_fireworks = True
        break

if is_enough_fireworks:
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can’t make the perfect firework show.')
if len(firework_efects) > 0:
    print(f'Firework Effects left: {", ".join([str(el) for el in firework_efects])}')
if len(firework_explosive_power) > 0:
    print(f'Explosive Power left: {", ".join([str(el) for el in firework_explosive_power])}')
print(f'Palm Fireworks: {palm_counter}')
print(f'Willow Fireworks: {willow_counter}')
print(f'Crossette Fireworks: {crossette_counter}')
