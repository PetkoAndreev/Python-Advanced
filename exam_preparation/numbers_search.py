def numbers_searching(*args):
    duplicate_nums = []
    unique_nums = []
    min_num = min(args)
    max_num = max(args)
    for num in range(min_num, max_num + 1):
        if num not in unique_nums:
            unique_nums.append(num)
        if num not in args:
            last_missing_num = num
        if args.count(num) > 1:
            duplicate_nums.append(num)
        duplicate_nums = sorted(duplicate_nums)
    result = [last_missing_num, duplicate_nums]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
