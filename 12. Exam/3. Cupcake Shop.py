from collections import deque


def delivery(products, args):
    for product in args:
        products.append(product)
    return products


def sell(products, args):
    products = deque(products)
    if len(args) == 1 and str(args[0]).isdigit():
        for i in range(int(args[0])):
            products.popleft()
    elif len(args) == 0:
        products.popleft()
    elif len(args) != 0:
        for product in args:
            if product in products:
                products = list(filter(lambda s: s != product, products))
    products = list(products)
    return products


def stock_availability(products, action, *args):
    if action == 'delivery':
        products = delivery(products, args)
    elif action == 'sell':
        products = sell(products, args)
    return products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

'''
Results:
['choco', 'vanilla', 'banana', 'caramel', 'berry']
['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
['vanilla', 'banana']
[]
['banana']
['cookie', 'banana']
['chocolate', 'vanilla', 'banana']
'''
