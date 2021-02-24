'''
Reformat the given code:
numbers_list = input().split(", ")
result = 0

for i in range(numbers_list):
    number = numbers_list[i + 1]
    if number < 5:
        result *= number
    elif number > 5 and number > 10:
        result /= number

print(result)
'''

numbers_list = list(map(int, input().split(', ')))
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    else:
        result /= number

print(f'{result:.0f}')