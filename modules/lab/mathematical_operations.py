from Modules import math_operations

num1, sign, num2 = input().split()
num1 = float(num1)
num2 = int(num2)

if sign == '+':
    result = math_operations.my_sum(num1, num2)
elif sign == '-':
    result = math_operations.subtract(num1, num2)
elif sign == '*':
    result = math_operations.multiply(num1, num2)
elif sign == '/':
    result = math_operations.divide(num1, num2)
elif sign == '^':
    result = math_operations.power(num1, num2)
else:
    result = None

print(f'{result:.2f}')