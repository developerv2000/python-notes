import heapq

nums = [22, 54, 3, 2351, 98234, 20, 12, 100000, -97, -56, 13]
print(heapq.nlargest(3, nums))  # [100000, 98234, 2351]
print(heapq.nsmallest(3, nums))  # [-97, -56, 3]

users = [
    {'name': 'Bob', 'age': 26, 'points': 98},
    {'name': 'Nina', 'age': 15, 'points': 65},
    {'name': 'Ksyu', 'age': 22, 'points': 76},
    {'name': 'Mila', 'age': 32, 'points': 100},
    {'name': 'Debra', 'age': 20, 'points': 40},
]

print(heapq.nlargest(3, users, key=lambda u: u['points']))
print(heapq.nsmallest(3, users, key=lambda u: u['age']))

print(sorted(users, key=lambda u: u['age']))

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)