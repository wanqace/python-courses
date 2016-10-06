#!/usr/bin/env python
f = open('/Users/i_voytas/Downloads/access.log')
bytes = 0
for line in f:
    s = line.split()[8:10]
    if s[0] == '200' and s[1].isdigit():
        bytes += int(s[1])
print bytes

def g(file_name):
    f = open(file_name)
    l = f.readline()
    while l:
        yield l.split()[0]
        l = f.readline()
    f.close()

for i in g('/Users/i_voytas/Downloads/access.log'):
    print i
