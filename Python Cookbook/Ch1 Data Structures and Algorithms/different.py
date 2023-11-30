# Naming a Slice
info = '2021-04-01 12:30:00 Tajikistan Dushanbe'
date = info[0:10]
address = info[20:]

# Instead of hard coding use slice names
date_slice = slice(0, 10)
address_slice = slice(20, None)
print(info[address_slice])
address_slice.start()  # 20. Also available stop, step
