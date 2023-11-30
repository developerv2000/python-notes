import os
import sys

path = 'D:/projects/test.txt'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('temp', 'data', os.path.basename(path)))
print(os.path.splitext(path))

print(os.path.exists(path))
print(os.path.isdir(path))
print(os.listdir('.'))

files = [file for file in os.listdir('/')
         if os.path.isfile(os.path.join('/', file))]

print(files)
# print(os.stat(path))
print(sys.getfilesystemencoding())

print(open('D:/test.txt', 'w'))