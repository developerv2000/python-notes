text = 'Today i saw a fox'
replaced = text.replace('Today', 'Yesterday')

# rewrite dates of the form “11/27/2012” as “2012-11-27
# using re.sub() function
import  re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
replaced = datepat.sub( r'\3-\2-\1', text)

# For more complicated substitutions, it’s possible to specify a substitution callback function
# instead. For example:
from calendar import month_abbr
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

def change_month(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

replaced = datepat.sub(change_month, text)

# If you want to know how many substitutions were made in addition to getting the
# replacement text, use re.subn() instead. For example:
newtext, subs_numb = datepat.subn(change_month, text)  # subs_numb = 2


# Searching and Replacing Case-Insensitive Text
text = 'UPPER PYTHON, lower python, Mixed Python'
pattern = re.compile(r'python', flags=re.IGNORECASE)
matches = re.findall(pattern, text)  # ['PYTHON', 'python', 'Python']

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

replaced = pattern.sub(matchcase('snake'), text)
print(replaced)

# Highlight word example
text = 'Hello FRIEND. How are you? Me and my friends are going to swim. Lets go with us!'
keyword = r'friend'

def highlight_match(m):
    return '<span class="highlighted>' + m.group() + '</span>'

replaced = re.sub(keyword, highlight_match, text, flags=re.IGNORECASE)
print(replaced)

