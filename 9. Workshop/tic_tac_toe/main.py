import setup
from play_engine import play


if __name__ == '__main__':
    setup.setup()
    play()
    new_game = input(f'Do you want to play a new game? y/n: ')
    while new_game not in ('yn'):
        input(f'Do you want to play a new game? lease enter "y" or "n": ')
    while new_game == "y":
        setup.setup()
        play()
        new_game = input(f'Do you want to play a new game? y/n: ')

    print(setup.game_counter)
    print('Bye!')