class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

    def error_message(self):
        return "Minimum text length > " + str(self.atleast) + ", but you entered: " + str(self.length) + " symbols"


try:
    text = input("Input text length > 3: ")
    if len(text) < 4:
        raise ShortInputException(len(text), 3)
except ShortInputException as ex:
    print(ex.error_message())
else:  # if no exceptions
    print("No exceptions")
finally:
    print("This block will run anyway")


# Automatically close file on finally block (exceptions)
with open("files/pickling.txt") as f:
    for line in f:
        print(line, end="")