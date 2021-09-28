queries = int(input())

s = []

for i in range(1, queries + 1):
    data = input().split()
    command = data[0]
    if command == '1':
        element = int(data[1])
        s.append(element)
    elif command == '2':
        if len(s) > 0:
            s.pop()
    elif command == '3':
        if len(s) > 0:
            print(max(s))
    elif command == '4':
        if len(s) > 0:
            print(min(s))

while s:
    if len(s) > 1:
        print(s.pop(), end = ', ')
    else:
        print(s.pop())