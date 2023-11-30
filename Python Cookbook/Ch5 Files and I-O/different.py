import io

with open(__file__, 'rt') as f:
    content = f.read()  # all content
    for line in f:
        pass
        # print(line)

f = open(__file__, 'rt', encoding='ascii', errors='replace')
content = f.read()
# print('Hello World!', file=f)
f.close()

s = io.StringIO('Hello World\n')
print(s.getvalue())

