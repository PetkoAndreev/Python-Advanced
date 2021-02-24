vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union([s.upper() for s in vowels])

input_data = input()
result = [s for s in input_data if s not in vowels]

print(''.join(result))