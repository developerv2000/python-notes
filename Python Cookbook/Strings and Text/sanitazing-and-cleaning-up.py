# Stripping Unwanted Characters from Strings
s = ' hello world \n'
s.strip()  # 'hello world'
s.lstrip()  # 'hello world \n'

t = '----hello----'
t.strip('-')

# To remove whitespace from middle use regex
import re
s = ' hello       world \n'
replaced = re.sub(r'\s+', ' ', s)

# It is often the case that you want to combine string stripping operations with some other
# kind of iterative processing, such as reading lines of data from a file. If so, this is one
# area where a generator expression can be useful. For example:
with(open(__file__) as f):
    lines = [line.strip() for line in f]


# Sanitize users submitted form data
s = 'pýtĥöñ\fis\tawesome\r\n'

# The first step is to clean up the whitespace. To do this, make a small translation table
# and use translate():
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None
}

translated = s.translate(remap)  # 'pýtĥöñ is awesome\n'

# Second step is to remove all combining characters
import unicodedata
import sys

normalized = unicodedata.normalize('NFD', translated)  # 'pýtĥöñ is awesome\n'

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
normalized2 = normalized.translate(cmb_chrs)  # 'python is awesome\n'


# As another example, here is a translation table that maps all Unicode decimal digit
# characters to their equivalent in ASCII:
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                   for c in range(sys.maxunicode)
                   if unicodedata.category(chr(c)) == 'ND'}

# Arabic digits
digits = '\u0661\u0662\u0663'
digits_translated = digits.translate(digitmap)  # 123


# Yet another technique for cleaning up text involves I/O decoding and encoding functions.
s = 'pýtĥöñ is awesome\n'
normalized = unicodedata.normalize('NFD', s)
cleaned = normalized.encode('ascii', 'ignore').decode('ascii')  # python is awesome
