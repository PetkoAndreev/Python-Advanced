def get_int_nums():
    return [int(num) for num in input().split()]


def get_min_max_sum_values(nums):
    max_num = max(nums)
    min_num = min(nums)
    sum_nums = sum(nums)
    return max_num, min_num, sum_nums


def print_result(max_num, min_num, sum_nums):
    print(f'The minimum number is {min_num}')
    print(f'The maximum number is {max_num}')
    print(f'The sum number is: {sum_nums}')


nums = get_int_nums()
max_num, min_num, sum_nums = get_min_max_sum_values(nums)
print_result(max_num, min_num, sum_nums)