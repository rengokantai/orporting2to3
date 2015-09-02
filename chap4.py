import sys

__author__ = 'Hernan Y.Ke'
from builtins import int
import array
import io



print(type(u'name'))  # str, but in python2 it will print unicode

#4-3
#str.decode()   byte to unicode
#str.encode()  unicode to byte

print(b"abc".decode())
print("abc".encode())

with open('./sample.txt', 'rb') as w:
    for i in w.readline():
        print(i)
print("====================")

with io.open('./sample.txt', mode='rb') as w:
    for i in w.readline():
        print(i)

print("====================")

# with io.open('./sample.txt',encoding='utf-16') as w:
#     w.read(2)
# #4-4
# print(w)

sys.intern("abc")