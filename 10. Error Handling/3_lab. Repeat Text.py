word = input()
repeat_times = input()
try:
    result = word*int(repeat_times)
    print(result)
except ValueError:
    print('Variable times must be an integer')