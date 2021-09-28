from math import log


def calc_log(num, base):
    if base == 'natural':
        return f'{log(num):.2f}'
    else:
        return f'{log(num, int(base)):.2f}'
