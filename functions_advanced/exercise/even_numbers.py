def get_int_nums():
    return [int(num) for num in input().split()]


def get_even_values(nums):
    nums = list(filter(lambda s: s % 2 == 0, nums))
    return nums


def print_result(nums):
    print(nums)

float_nums = get_int_nums()
abs_nums = get_even_values(float_nums)
print_result(abs_nums)