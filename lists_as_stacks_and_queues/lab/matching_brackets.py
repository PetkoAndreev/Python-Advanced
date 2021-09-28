input_data = input()

s = []

for i in range(len(input_data)):
    if input_data[i] == '(':
        s.append(i)
    elif input_data[i] == ')':
        print(input_data[s.pop():i+1])