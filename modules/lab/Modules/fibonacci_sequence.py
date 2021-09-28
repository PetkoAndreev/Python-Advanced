seq = [0, 1]


def create_fibonacci(num):
    global seq
    seq = [0, 1]
    if num == 0:
        return [0]
    elif num == 1:
        return seq
    else:
        for i in range(2, num):
            seq.append(seq[-2] + seq[-1])
        return seq


def locate_number(num):
    if num in seq:
        return f'The number - {num} is at index {seq.index(num)}'
    else:
        return f'The number {num} is not in the sequence'
