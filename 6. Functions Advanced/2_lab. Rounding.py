def get_float_nums():
    return [float(num) for num in input().split()]


def get_round_values(nums):
    nums = [round(num) for num in nums]
    return nums


def print_result(nums):
    print(nums)

float_nums = get_float_nums()
round_nums = get_round_values(float_nums)
print_result(round_nums)