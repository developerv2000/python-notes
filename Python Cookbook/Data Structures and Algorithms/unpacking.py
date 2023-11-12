t = ('Bobur', 'Nuridinov')
name, surname = t


def drop_first_last(grades):
    first, *middle, last = grades
    return middle

record = ('Dave', 'dave@mail.com', 98382928932, 794174974)
name, email, *phones = record


records = [
    ('sum', 1, 2, 3),
    ('multiple', 2, 3, 5),
    ('sum', 3, 6, 9)
]

for operation, *args in records:
    if operation == 'sum':
        summary = sum(args)
    elif operation == 'multiple':
        summary = 1
        for arg in args:
            summary = summary * arg


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

record = ('ACME', 55, 66, 77, (12, 11, 2023))
name, *_, (*_, year) = record