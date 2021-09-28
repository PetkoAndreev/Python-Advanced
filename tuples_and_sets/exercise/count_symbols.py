input_data = input()
symbols = {}

def count_symbols(data):
    for symbol in data:
        if symbol not in symbols:
            symbols[symbol] = 0
        symbols[symbol] += 1
    return dict(sorted(symbols.items(), key=lambda s: s[0]))


def print_data(symbols):
    for symbol, count in symbols.items():
        print(f'{symbol}: {count} time/s')


symbols = count_symbols(input_data)
print_data(symbols)