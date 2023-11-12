my_list = [1,2,3,4,5]  # changeable
my_tuple = ("koko", 'kaka', "nono")  # unchangeable
my_dict = {'name': 'Bobur', 'age': 27}
my_set = {'red', 'orange', 'purple'}  # unrepeatable

dictionary_list = [
    {
        "name": "Bobur",
        "surname": "Niridinov",
        "age": 24,
    },

    {
        "name": "Kimki",
        "surname": "Kimchi",
        "age": 33,
    },
]

for contact in dictionary_list:
    formatted = '{0} {1} is {2} years old'.format(contact['name'], contact['surname'], contact['age'])

shop_list = ['apple', 'mango', 'banana', 'potato', 'carrot']
cropped = shop_list[1:-1:2]

if 'banana' in shop_list:
    buy_banana = True

if 'milk' not in shop_list:
    ignore_milk = True

my_set2 = my_set.copy()
my_set2.add('yellow')
set_intersections = my_set2.intersection(my_set)

my_list2 = my_list[:]  # copy

# list generators
my_list3 = [2*i for i in my_list2 if i > 2]  # [6, 8, 10]


joined = '__'.join(shop_list)  # apple__mango__banana__potato__carrot
