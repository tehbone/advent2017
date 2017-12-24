#!/usr/bin/python
import sys

def get_max(banks):
    i = 0
    v = banks[0]
    for j in xrange(1, len(banks)):
        if banks[j] > v:
            v = banks[j]
            i = j

    return v, i

def get_banks():
    with open('input.txt', 'r') as f:
        return [int(x) for x in f.readline().split()]

def main():
    cache = set()
    check_cache = True
    num_iter = 0
    if len(sys.argv) > 1:
        banks = [int(x) for x in sys.argv[1::]]
    else:
        banks = get_banks()

    num_banks = len(banks)
    while True:
        v, i = get_max(banks)
        r = v % num_banks
        c = (v - r) / num_banks
        banks[i] = 0
        banks = [ x + c for x in banks]
        for j in xrange(i + 1, i + 1 + r):
            k = j % num_banks
            banks[k] = banks[k] + 1

        key = ' '.join([str(x) for x in banks])
        num_iter = num_iter + 1
        if check_cache:
            if key in cache:
                saved_key = key
                num_iter = 0
                check_cache = False
            cache.add(key)
        elif saved_key == key:
            break;

    print('Number of iterations: {}'.format(num_iter))
    
if __name__ == '__main__':
    main()
