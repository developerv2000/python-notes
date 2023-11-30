# To perform conversions and arithmetic involving different units of time, use the date
# time module. For example, to represent an interval of time, create a timedelta instance
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days  # 2
c.seconds  # 37800


# If you need to represent specific dates and times, create datetime instances and use the
# standard mathematical operations to manipulate them.
from datetime import datetime
a = datetime(2012,9,23)
a + timedelta(days=10)  # 2012-10-03 00:00:00

b = datetime(2012, 12, 21)
d = b - a  # 89 days, 0:00:00

now = datetime.today()  # 2023-10-21 19:43:21.620034
now + timedelta(minutes=10)

# When making calculations, it should be noted that datetime is aware of leap years. For
# example:
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)  # 2 days, 0:00:00

a = datetime(2013, 3, 1)
b = datetime(2013, 2, 28)
print(a - b)  # 1 day, 0:00:00

# For most basic date and time manipulation problems, the datetime module will suffice.
# If you need to perform more complex date manipulations, such as dealing with time
# zones, fuzzy time ranges, calculating the dates of holidays, and so forth, look at the
# dateutil module


# Ideally, it would be nice to create a function that works like the built-in range() function,
# but for dates. Fortunately, this is extremely easy to implement using a generator:
def date_range(start, stop, step):
    while start < stop :
        yield start
        start += step

for d in (date_range(datetime(2023,1,1), datetime(2023,2,5),
                        timedelta(hours=12))):
    print(d)


# Many recipes skipped for this chapter. Checkout book for more examples
