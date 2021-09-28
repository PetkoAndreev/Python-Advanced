brackets_data = list(input())
brackets = []

for i in range(len(brackets_data)):
    if brackets_data[i] in '([{':
        brackets.append(brackets_data[i])
    if brackets != []:
        if brackets_data[i] == ')' and brackets[-1] == '(':
            brackets.pop()
        elif brackets_data[i] == ']' and brackets[-1] == '[':
            brackets.pop()
        elif brackets_data[i] == '}' and brackets[-1] == '{':
            brackets.pop()
    else:
        brackets.append(brackets_data[i])
        break

if len(brackets) != 0:
    print('NO')
else:
    print('YES')