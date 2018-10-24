#/usr/bin/env python3.6
# -*- coding:utf-8 -*-

__author__ = 'Jagger'


print('Hello Python world!\n')
print('*' * 10)
for i in range(5):
    print('*        *')
print('*' * 10)
print('*\n' * 6)



a = 176
b = 219
print(chr(b),chr(a),chr(a),chr(a),chr(b))
print(chr(a),chr(b),chr(a),chr(b),chr(a))
print(chr(a),chr(a),chr(b),chr(a),chr(a))
print(chr(a),chr(b),chr(a),chr(b),chr(a))
print(chr(b),chr(a),chr(a),chr(a),chr(b))


import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print('')

for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print('')




import sys
for i in range(8):
    for j in range(8):
        if(i + j) % 2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write(' ')
    print('')
