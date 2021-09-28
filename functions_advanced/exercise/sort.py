def get_int_nums():
    return [int(num) for num in input().split()]


def get_sort_values(nums):
    nums = list(sorted(nums, key=lambda s: s))
    return nums


def print_result(nums):
    print(nums)

float_nums = get_int_nums()
abs_nums = get_sort_values(float_nums)
print_result(abs_nums)