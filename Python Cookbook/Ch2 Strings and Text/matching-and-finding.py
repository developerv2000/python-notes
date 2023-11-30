# Matching Text at the Start or End of a String
filename = 'spam.txt'
filename.startswith('spam')  # True
filename.endswith('.py')  # False

import os
filenames = os.listdir('../Data Structures and Algorithms')
python_files = [name for name in filenames if name.endswith('.py')]
any(name.endswith(('.py', '.python')) for name in filenames)  # True


# Matching Strings Using Shell Wildcard Patterns
from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')  # True
fnmatch('foo.txt', '??o.txt')  # True
fnmatch('foo.txt', '[!poo,doo]*.txt')  # True
fnmatch('Dat45.csv', 'Dat[0-9]*')  # True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
names_matched = [name for name in names if fnmatch(name, 'Dat*.csv')]  # ['Dat1.csv', 'Dat2.csv']

# Normally, fnmatch() matches patterns using the same case-sensitivity rules as the system’s
# underlying filesystem (which varies based on operating system). For example:

# On OS X (Mac)
fnmatch('foo.txt', '*.TXT')  # False

# On Windows
fnmatch('foo.txt', '*.TXT')  # True

# If this distinction matters, use fnmatchcase() instead. It matches exactly based on the
# lower- and uppercase conventions that you supply:
fnmatchcase('foo.txt', '*.TXT')  # False

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

streets = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
clark_street = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]


# Matching and Searching for Text Patterns
text = 'Once upon a time'
text.find('upon')  # 5
text.find('sun')  # -1

# Find using regex
import re
text1 = '11/27/2012'

if re.match(r'\d+/\d+/\d+', text1):
    matched = True
else:
    matched = False

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    matched = True
else:
    matched = False

# Find All using regex. findall function doesnt support grouping (use finditer instead for grouping)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)  # ['11/27/2012', '3/13/2013']

# When defining regular expressions, it is common to introduce capture groups by enclosing
# parts of the pattern in parentheses. For example:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
m.group(0)  # '11/27/2012'
m.group(1)  # '11'
m.group(2)  # '27

# The findall() method searches the text and finds all matches, returning them as a list.
# If you want to find matches iteratively, use the finditer() method instead. For example:
for m in datepat.finditer(text):
    group = m.groups()


# Greeding control of regex expressions
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)  # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)  # ['no." Phone says "yes.']
# To fix this, add the ? modifier after the * operator in the pattern, like this:
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)  # ['no.', 'yes.']


# Writing a Regular Expression for Multiline Patterns
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
        multiline comment */
        '''

comment.findall(text1)  # [' this is a comment ']
comment.findall(text2)  # []
# To fix the problem, you can add support for newlines. For example:
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)  # [' this is a\n        multiline comment ']

# The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes
# the . in a regular expression match all characters, including newlines. For example:
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
# Using the re.DOTALL flag works fine for simple cases, but might be problematic if you’re
# working with extremely complicated patterns
