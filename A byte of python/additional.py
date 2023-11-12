# Return multiple results using tuple
def get_error_details():
    return 2, "Error description"


errnum, errinfo = get_error_details()

# Multiple declaration
var1, *var2 = [1, 2, 3, 4]
# a = 1
# b = 2, 3, 4


# The assert keyword is used when debugging code
debug_var = 25
# debug_var = 26

assert debug_var == 25, "debug_var must equal to 25!"

# The repr function returns a printable representation of the given object
printable_obj = ['item1', 'item2']
repr(printable_obj)

# Escape special characters
print(r"Next line character wont work \n, check it")