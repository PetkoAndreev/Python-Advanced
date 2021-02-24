input_data = input()

s = []

for i in range(len(input_data)-1, -1, -1):
    s.append(input_data[i])

print(''.join(s))