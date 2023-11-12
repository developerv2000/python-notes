# Mapping Keys to Multiple Values
from collections import defaultdict

list_dict = defaultdict(list)
list_dict['a'].append(1)
list_dict['a'].append(2)
list_dict['b'].append(5)
list_dict['b'].append(5)

print(list_dict)  # {'a': [1, 2], 'b': [5, 5]}

set_dict = defaultdict(set)
set_dict['a'].add(1)
set_dict['a'].add(2)
set_dict['b'].add(5)
set_dict['b'].add(5)

print(set_dict)  # {'a': {1, 2}, 'b': {5}}


# exactly preserves the original insertion order of data when iterating.
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3


# Calculating with Dictionaries
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = prices[min(prices, key=lambda k: prices[k])]  # 10.75 (hard way and returns only key)
max_price = max(zip(prices.values(), prices.keys()))  # (612.78, 'AAPL') easy way!


# Finding Commonalities in Two Dictionaries
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

common = a.keys() & b.keys()
diff = a.keys() - b.keys()
common_pairs = a.items() & b.items()
# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}  # {'x': 1, 'y': 2}


# Removing Duplicates from a Sequence while Maintaining Order
def remove_list_duplicates(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(remove_list_duplicates(a))  # [1, 5, 2, 9, 10]

def remove_dict_duplicates(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
        seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(remove_dict_duplicates(a, key=lambda d: (d['x'],d['y'])))


# Determining the Most Frequently Occurring Items
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)  # {'eyes': 8, 'the': 5, 'look': 4 ...}
word_counts['look']  # 4
top_two = word_counts.most_common(2)  # {'eyes': 8, 'the': 5}

# insert more words
more_words = ['why','are','you','not','looking','in','my','eyes', 'kolobok']
word_counts.update(more_words)


# Sorting a List of Dictionaries by a Common Key
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_uid = sorted(rows, key=lambda r: r['uid'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

from operator import itemgetter
# itemgetter runs a bit faster than lambda function
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))


# Sorting Objects Without Native Comparison Support
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'User({})'.format(self.name)

users = [User('Bob'), User('Anya'), User('Kimchin')]
sorted_users = sorted(users, key=lambda u: u.name)

from operator import attrgetter
# attrgetter runs a bit faster than lambda function
sorted_users = sorted(users, key=attrgetter('name'))  # also supports multiple attrs


# Grouping Records Together Based on a Field
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from itertools import groupby
rows_sorted = sorted(rows, key=itemgetter('date'))
rows_grouped = groupby(rows_sorted, key=itemgetter('date'))

for date, items in rows_grouped:
    print(date)
    for i in items:
        print('     ', i)

# Grouping using defaultdict
rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['date']].append(row)
# print(rows_by_date['07/01/2012'])


# Filtering Sequence Elements
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# List comprehension expression
mylist2 = [i for i in mylist if i > 0]  # [1, 4, 10, 2, 3]
mylist3 = [i if i > 0 else 0 for i in mylist]  # [1, 4, 0, 10, 0, 2, 3, 0]

# Use generators for better performance
mylist2 = list(i for i in mylist if i > 0)  # generator

def is_even_number(number):
    return True if number % 2 == 0 else False

# Using built-in filter function
even_numbers = list(filter(is_even_number, mylist))
print(even_numbers)

# Filtering using an iterable and an accompanying Boolean selector sequence as input
from itertools import compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [i > 5 for i in counts]  # [False, False, True, False, False, True, True, False]
list(compress(addresses, more5))  # ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']


# Extracting a Subset of a Dictionary
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
prices2 = {key: value for key, value in prices.items() if value > 200}  # {'AAPL': 612.78, 'IBM': 205.55}

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
prices3 = {key:value for key,value in prices.items() if key in tech_names}
prices2 = {key:prices[key] for key in prices.keys() & tech_names}  # slower than first method


# Mapping Names to Sequence Elements
from collections import namedtuple  # supports all usual tuple operations
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
new_subscriber = Subscriber('user@mail.ru', '2023/04/01')  # Subscriber(addr='user@mail.ru', joined='2023/04/01')
new_subscriber.addr  # user@mail.ru

# Good example
def calc_total_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]  # hardcoded
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def calc_total_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(rec)
        total += s.shares * s.price
    return total


# Transforming and Reducing Data at the Same Time
nums = [1,2,3,4,5,6]
nums_square_sum = sum(x * x for x in nums if x > 4)  # using generators (good way)
nums_square_sum2 = sum([x * x for x in nums])  # introduces an extra step and creates an extra list (bad way)
print(nums_square_sum)

import os
files = os.listdir('.//')
if any(name.endswith('.py') for name in files):
    print('There is python file!')
else:
    print('There is no python file!')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))  # type casting using generator

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(p['shares'] for p in portfolio)  # Returns 20
min_shares2 = min(portfolio, key=lambda s: s['shares'])  # Alternative: {'name': 'AOL', 'shares': 20}


# Combining Multiple Mappings into a Single Mapping
from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

chained = ChainMap(a,b)
chained['y']  # 2
chained['z']  # 3. If there are duplicate keys, the values from the first mapping get used.

a['y'] = 24
print(chained['y'])  # 24. A ChainMap uses the original dictionaries,

