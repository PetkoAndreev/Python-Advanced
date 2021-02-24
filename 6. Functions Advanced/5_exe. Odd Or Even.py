def get_nums():
    return [int(num) for num in input().split()]


def get_command_nums(command, nums):
    if command == 'Odd':
        return [s for s in nums if s % 2 != 0]
    elif command == 'Even':
        return [s for s in nums if s % 2 == 0]


def print_result(nums, filter_nums):
    print(sum(filter_nums) * len(nums))


command = input()
nums = get_nums()
filter_nums = get_command_nums(command, nums)
print_result(nums, filter_nums)