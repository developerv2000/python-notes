def total(a=5, *numbers, **phonebook):
    """
    Function documentation
    """
    print(total.__doc__)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)


def total2(initial=5, *numbers, extra_number):
    count = initial

    for number in numbers:
        count += number
    count += extra_number
    print(count)


total2(10, 1, 2, 3, extra_number=4)
total2(10, 1, 2, 3)  # error extra_number not defined

# Lambda function (small anonymous function)
multiplication = lambda a, b: a * b
print(multiplication(2, 20))  # 40
