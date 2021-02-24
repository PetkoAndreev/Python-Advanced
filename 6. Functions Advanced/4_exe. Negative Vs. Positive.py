def get_nums():
    return [int(num) for num in input().split()]


def get_positive_negative_nums(nums):
    positive_nums = [s for s in nums if s >= 0]
    negative_nums = [s for s in nums if s < 0]
    return negative_nums, positive_nums


def print_result(negative_nums, positive_nums):
    print(sum(negative_nums))
    print(sum(positive_nums))
    if abs(sum(negative_nums)) > sum(positive_nums):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


nums = get_nums()
negative_nums, positive_nums = get_positive_negative_nums(nums)
print_result(negative_nums, positive_nums)