nums = list(map(int, input().split()))
n = nums[0]
m = nums[1]


def input_lines(number):
    lines = set()
    for _ in range(number):
        lines.add(input())

    return lines


def print_data(result):
    for num in result:
        print(num)

n_set = input_lines(n)
m_set = input_lines(m)

result = n_set.intersection(m_set)
# result = n_set & m_set

print_data(result)