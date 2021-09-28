contact_list = {}


def input_contacts():
    data = input()
    while not data.isdigit():
        contact, phone = data.split('-')
        contact_list[contact] = phone
        data = input()
    return contact_list, data


def input_lines(number):
    lines = []
    for _ in range(number):
        lines.append(input())
    return lines

def print_data(contact_list, names_to_check):
    for name in names_to_check:
        if name in contact_list:
            print(f'{name} -> {contact_list[name]}')
        else:
            print(f'Contact {name} does not exist.')


contact_list, data = input_contacts()
number = int(data)
names_to_check = input_lines(number)
print_data(contact_list, names_to_check)