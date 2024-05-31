import heapq

def min_connection(length):
    if not length:
        return 0
    heapq.heapify(length)
    print(f'Cables length: {length}')
    total_cost = 0
    while len(length) >1 :
        print(f'Before operations: {length}')

        first = heapq.heappop(length)
        print(f'First min element was popped: {length}')
        
        second = heapq.heappop(length)
        print(f'Second min element was popped: {length}')

        cost = first + second
        print(f'Cost of marges two cabels({first} and {second}): {cost}')
        total_cost += cost
        
        heapq.heappush(length, cost)
        print(f'After push: {length}')
    
    print(f'Total cost: {total_cost}')

length = [34,21,10,10,8,2,7]

min_connection(length)
