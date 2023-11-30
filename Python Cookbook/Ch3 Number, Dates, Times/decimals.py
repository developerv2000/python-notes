# Rounding Numerical Values
round(1.23, 1)  # 1.2
round(-1.27, 1)  # -1.3
round(1.234678, 3)  # 1.235

# When a value is exactly halfway between two choices, the behavior of round is to round
# to the nearest even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.

# The number of digits given to round() can be negative, in which case rounding takes
# place for tens, hundreds, thousands, and so on. For example:
a = 1627731
round(a, -2)  # 1627700
round(a, -3)  # 1628000

# Don’t confuse rounding with formatting a value for output. If your goal is simply to
# output a numerical value with a certain number of decimal places, just specify the
# desired precision when formatting. For  example:
x = 1.23456
format(x, '0.2f')  # 1.23
'value is {:0.3f}'.format(x)  # value is 1.235

# Also, resist the urge to round floating-point numbers to “fix” perceived accuracy problems.
# For example, you might be inclined to do this:
a = 2.1
b = 4.2
c = a + b  # 6.300000000000001
c == 6.3  # False
round(c, 2)  # 6.3

# These errors are a “feature” of the underlying CPU and the IEEE 754 arithmetic performed
# by its floating-point unit. Since Python’s float data type stores data using the
# native representation, there’s nothing you can do to avoid such errors if you write your
# code using float instances.

# If you want more accuracy (and are willing to give up some performance), you can use
# the decimal module:
from decimal import Decimal
a = Decimal('2.1')
b = Decimal('4.2')
c = a + b  # Decimal('6.3')


# Formatting Numbers for Output
x = 1234.56789
format(x, '<10.1f')  # '1234.6 '
format(x, '0,.1f')  # 1,234.6
format(x, '0.2E')  # '1.23E+03'
'The value is {:0,.2f}'.format(x)  # '1.23E+03'

print(int.bit_length(250002))
