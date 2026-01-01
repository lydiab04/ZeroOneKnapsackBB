# Group Members:

# LYDIA YOSEPH             UGR/7809/15
# MESERET GHEBIRESILASSIE  UGR/0722/15
# MIKIYAS FASIL            UGR/9231/15
# SALEM GEBRU              UGR/6916/15

# Section - 2


from queue import Queue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

def compare(a, b):
    r1 = float(a.value) / a.weight
    r2 = float(b.value) / b.weight
    return r1 > r2

def bound(u, n, W, arr):
    
    if u.weight >= W:
        return 0

    profitBound = u.profit
    j = u.level + 1
    totWeight = int(u.weight)

    while j < n and totWeight + int(arr[j].weight) <= W:
        totWeight += int(arr[j].weight)
        profitBound += arr[j].value
        j += 1

    if j < n:
        profitBound += int((W - totWeight) * arr[j].value / arr[j].weight)

    return profitBound

def knapsack_solution(capacity, items, length):

    
    
    items.sort(key=lambda x: x.value / x.weight, reverse=True)


   
    q = Queue()
    u = Node(-1, 0, 0, 0)
    q.put(u)

   
    maxProfit = 0

   
    while not q.empty():
        u = q.get()

       
        if u.level == -1:
            v = Node(0, 0, 0, 0)

   
        if u.level == length - 1:
            continue

        
        v = Node(u.level + 1, u.profit +
                 items[u.level + 1].value, 0, u.weight + items[u.level + 1].weight)

        
        if v.weight <= capacity and v.profit > maxProfit:
            maxProfit = v.profit

       
        v.bound = bound(v, length, capacity, items)

        if v.bound > maxProfit:
            q.put(v)

        v = Node(u.level + 1, u.profit, 0, u.weight)

        v.bound = bound(v, length, capacity, items)

        if v.bound > maxProfit:
            q.put(v)

    return maxProfit



if __name__ == '__main__':
    capacity = 10
    items = [Item(2, 10), Item(4, 10), Item(
        6, 12), Item(9, 18)]
    length = len(items)

    print ("Maximum possible profit =", knapsack_solution(capacity, items, length))


