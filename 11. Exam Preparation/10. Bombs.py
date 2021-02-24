from collections import deque


def get_bomb_creation_check(bomb_effects, bomb_casings):
    datura_bombs = 0
    cherry_bobs = 0
    smoke_decoy = 0
    bombs_values = [40, 60, 120]
    bomb_pouch = False
    while len(bomb_effects) != 0 and len(bomb_casings) != 0:
        current_bomb_value = bomb_effects[0] + bomb_casings[-1]
        if current_bomb_value not in bombs_values:
            bomb_casings[-1] -= 5
        else:
            if current_bomb_value == 40:
                datura_bombs += 1
            elif current_bomb_value == 60:
                cherry_bobs += 1
            elif current_bomb_value == 120:
                smoke_decoy += 1
            bomb_effects.popleft()
            bomb_casings.pop()
        if datura_bombs >= 3 and cherry_bobs >= 3 and smoke_decoy >= 3:
            bomb_pouch = True
            break
    return bomb_effects, bomb_casings, bomb_pouch, datura_bombs, cherry_bobs, smoke_decoy


def print_result(bomb_effects, bomb_casings, bomb_pouch, datura_bombs, cherry_bobs, smoke_decoy):
    if bomb_pouch:
        print('Bene! You have successfully filled the bomb pouch!')
    else:
        print('You don\'t have enough materials to fill the bomb pouch.')
    if bomb_effects:
        print(f'Bomb Effects: {", ".join(str(s) for s in bomb_effects)}')
    else:
        print('Bomb Effects: empty')
    if bomb_casings:
        print(f'Bomb Casings: {", ".join(str(s) for s in bomb_casings)}')
    else:
        print('Bomb Casings: empty')
    print(f'Cherry Bombs: {cherry_bobs}')
    print(f'Datura Bombs: {datura_bombs}')
    print(f'Smoke Decoy Bombs: {smoke_decoy}')


bomb_effects = deque([int(s) for s in input().split(', ')])
bomb_casings = [int(s) for s in input().split(', ')]
bomb_effects, bomb_casings, bomb_pouch, datura_bombs, cherry_bobs, smoke_decoy = get_bomb_creation_check(bomb_effects,
                                                                                                         bomb_casings)
print_result(bomb_effects, bomb_casings, bomb_pouch, datura_bombs, cherry_bobs, smoke_decoy)
