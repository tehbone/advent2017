#!/usr/bin/python
import sys

DEFAULT_FILENAME='input.txt'

def get_passphrase(filename):
    with open(filename, 'r') as f:
        for line in f:
            l = line.strip()
            if l:
                yield l

def is_passphrase_valid(passphrase):
    s = set()
    for word in passphrase.split():
        if word in s:
            return False
        s.add(word)

    return True

def main(filename):
    c = 0
    for passphrase in get_passphrase(filename):
        if is_passphrase_valid(passphrase):
            c = c + 1

    print('Num valid: {}'.format(c))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = DEFAULT_FILENAME

    main(filename)
