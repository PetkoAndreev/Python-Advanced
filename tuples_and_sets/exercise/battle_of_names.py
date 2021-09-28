num = int(input())


def input_lines(number):
    odd_nums = set()
    even_nums = set()
    for num in range(1, number + 1):
        name = input()
        sum_chars = 0
        for char in name:
            sum_chars += ord(char)
        if (sum_chars // num) % 2 != 0:
            odd_nums.add(sum_chars // num)
        else:
            even_nums.add(sum_chars // num)
    return odd_nums, even_nums


def print_data(odd_nums, even_nums):
    result = set()
    if sum(odd_nums) == sum(even_nums):
        result = odd_nums.union(even_nums)
    elif sum(odd_nums) > sum(even_nums):
        result = odd_nums.difference(even_nums)
    elif sum(odd_nums) < sum(even_nums):
        result = odd_nums.symmetric_difference(even_nums)
    print(', '.join(map(str, result)))


odd_nums, even_nums = input_lines(num)
print_data(odd_nums, even_nums)