# Manually Consuming an Iterator
items = [1, 2, 3, 4]
it = iter(items)
while True:
    el = next(it, None)
    if el is None:
        break
    # print(el)


# Creating New Iteration Patterns with Generators
def float_generator(start, stop, increment):
    while start < stop:
        yield start
        start += increment


for numb in float_generator(1,4,0.5):
    pass
    # print(numb)

numbs_list = list(float_generator(1,4,0.5))
print(sum(numbs_list))


# Taking a Slice of an Iterator
nums = float_generator(1, 99999999, 0.5)
# nums[10:20] # Error

import itertools
for num in itertools.islice(nums, 4, 8):
    pass
    # print(num)

nums = float_generator(1, 99999999, 0.5)
numbs_list = list(itertools.islice(nums, 2, 6))
print(numbs_list)


items = ['a', 'b', 'c']
from itertools import combinations
for c in combinations(items, 2):
    print(c)


headers = ['name', 'shares', 'prices']
values = ['ACME', 100, 499]
dictioned = dict(zip(headers, values))
print(dictioned)


from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
