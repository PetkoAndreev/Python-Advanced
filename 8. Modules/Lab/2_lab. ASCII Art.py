from pyfiglet import figlet_format


def print_art():
    input_data = input()
    result = figlet_format(input_data)
    print(result)


print_art()
