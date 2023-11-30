import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values)

# To take a sampling of N items where selected items are removed from further consideration,
# use random.sample() instead:
random_three = random.sample(values, 3)  # [4, 3, 1]

# If you simply want to shuffle items in a sequence in place, use random.shuffle():
random.shuffle(values)  # [3, 5, 2, 1, 6, 4]
random.randint(1, 5)  # 4

# To produce uniform floating-point values in the range 0 to 1, use random.random():
random.random()  # 0.43074643879137353
