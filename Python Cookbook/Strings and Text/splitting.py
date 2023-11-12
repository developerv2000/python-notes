# Using single delimiter
'file, directory, path, extension'.split(', ')  # ['file', 'directory', 'path', 'extension']

# using Multiple Delimiters
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']