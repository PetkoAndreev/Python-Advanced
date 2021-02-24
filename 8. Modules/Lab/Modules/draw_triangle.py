def draw_firs_half(num):
    for i in range(1, num + 1):
        result = []
        for j in range(1, i + 1):
            result.append(str(j))
        print(' '.join(result))


def draw_second_half(num):
    for i in range(num - 1, 0, -1):
        result = []
        for j in range(1, i + 1):
            result.append(str(j))
        print(' '.join(result))
