num_lists = [s.split() for s in input().split('|')[::-1]]
result = []
for num_list in num_lists:
    for num in num_list:
        result.append(num)
print(' '.join(result))