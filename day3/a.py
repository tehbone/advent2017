#!/usr/bin/python
import sys

def main(num):
    i = 0
    c = 1
    l = 1
    while num > c:
        i = i + 1
        l = (i*2 + 1)
        c = l ** 2

    e = c
    b = e
    while num < b:
        e = b
        b = b - l + 1
    print('Dist is {}'.format(i + abs(num - (e+b)/2)))

if __name__ == '__main__':
    main(int(sys.argv[1]))
