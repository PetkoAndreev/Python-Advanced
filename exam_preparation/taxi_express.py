from collections import deque


def tend_customers(customers, taxi):
    total_time = 0
    while customers:
        if taxi[-1] >= customers[0]:
            total_time += customers[0]
            taxi.pop()
            customers.popleft()
        else:
            taxi.pop()
        if len(taxi) == 0:
            break

    return customers, taxi, total_time


def print_result(taxi, customers, total_time):
    if len(customers) != 0:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join(str(s) for s in customers)}')
    else:
        print('All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')


customers = deque([int(s) for s in input().split(', ')])
taxi = [int(s) for s in input().split(', ')]
customers, taxi, total_time = tend_customers(customers, taxi)
print_result(taxi, customers, total_time)
