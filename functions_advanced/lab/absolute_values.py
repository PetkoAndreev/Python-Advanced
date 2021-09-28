def get_float_nums():
    return [float(num) for num in input().split()]


def get_abs_values(nums):
    nums = [abs(num) for num in nums]
    return nums


def print_result(nums):
    print(nums)

float_nums = get_float_nums()
abs_nums = get_abs_values(float_nums)
print_result(abs_nums)