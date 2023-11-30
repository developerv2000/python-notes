s1 = 'Spicy Jalape\u00f1o'  # 'Spicy Jalapeño'
s2 = 'Spicy Jalapen\u0303o'  # 'Spicy Jalapeño'
s1 == s2  # False
len(s1)  # 14
len(s2)  # 15

# Having multiple representations is a problem for programs that compare strings. In
# order to fix this, you should first normalize the text into a standard representation using
# the unicodedata module:

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1 == t2  # True

# Python also supports the normalization forms NFKC and NFKD, which add extra compatibility
# features for dealing with certain kinds of characters. For example:
s = '\ufb01'  # 'fi' (A single character )
normalized = unicodedata.normalize('NFD', s)  # 'fi' (A single character )
len(normalized)  # 1

normalized = unicodedata.normalize('NFKD', s)  # 'fi' (Two symbols)
len(normalized)  # 2
