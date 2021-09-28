numbers = input().split()

s = []

for i in range(len(numbers)):
    s.append(numbers[i])

while s:
    print(s.pop(), end = ' ')