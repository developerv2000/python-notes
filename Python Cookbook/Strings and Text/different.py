# Aligning Text Strings
text = 'Hello World'
text.rjust(15)  #     Hello World
text.center(20, '*')  # ****Hello World*****

format(text, '>15')  #     Hello World
format(text, '*^20')  # ****Hello World*****

# These format codes can also be used in the format() method when formatting multiple
# values. For example:
'{:>10} {:>10}'.format('Hello', 'World')  #      Hello      World

# One benefit of format() is that it is not specific to strings. It works with any value,
# making it more general purpose. For instance, you can use it with numbers:
x = 1.2345
format(x, '*^10')  # **1.2345**

# In new code, you should probably prefer the use of the format() function or
# method. Moreover, format() is more general purpose than using the jlust(), rjust(), or
# center() method of strings in that it works with any kind of object.


# Combining and Concatenating Strings
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)  # Is Chicago Not Chicago?'
','.join(parts)  # Is,Chicago,Not,Chicago?

a = 'Is Chicago'
b = 'Not Chicago?'
c = a + b  # Is Chicago Not Chicago?


# Interpolating Variables in Strings
s = '{name} has {n} messages'
s.format(name='Guido', n=20)  # Guido has 20 messages

# Alternatively, if the values to be substituted are truly found in variables, you can use the
# combination of format_map() and vars(), as in the following:
s = '{name} has {n} messages'
name = 'Mister Bob'
n = 58
formatted = s.format_map(vars())  # Mister Bob has 58 messages

# One subtle feature of vars() is that it also works with instances. For example:
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

obj = Info('Bib', 78)
s = '{name} has {n} messages'
formatted = s.format_map(vars(obj))  # Bib has 78 messages


# Reformatting Text to a Fixed Number of Columns
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent=' '))


# Handling HTML
s = 'Elements are written as "<tag>text</tag>".'
import html

html.escape(s)  # Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.
html.escape(s, quote=False)  # Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

s = 'Spicy &quot;Jalape&#241;o&quot.'
html.unescape(s)  # Spicy "Jalapeño".


