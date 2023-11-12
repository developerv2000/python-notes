import pickle

# Store variable in file and get it back

shop_list_file = "files/pickling.txt"
shop_list = ["apple", "banana", "cherry"]

f = open(shop_list_file, "wb")
pickle.dump(shop_list, f)
f.close()

del shop_list

f = open(shop_list_file, "rb")
stored_shop_list = pickle.load(f)

print(stored_shop_list)


# Automatically close file on finally block (exceptions)
with open("files/pickling.txt") as f:
    for line in f:
        print(line, end="")