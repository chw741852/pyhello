from collections import deque
from math import pi
from math import isnan

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
print(fruits.index('banana', 4, 7))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print("fruits.pop(): ", fruits.pop())

queue = deque(['Eric', 'John', 'Micheal'])
queue.append('Terry')
queue.append('Graham')
print(queue.popleft())
print(queue.popleft())
print(queue)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

print([(str(round(pi, i))) for i in range(10)])

matrix = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12']
]
print([[row[i] for row in matrix] for i in range(4)])

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = list(filter(lambda x: not isnan(x), raw_data))
print(filtered_data)
