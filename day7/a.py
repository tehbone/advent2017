#!/usr/bin/python
import sys

class Program(object):
    def __init__(self, desc):
        super(Program, self).__init__()
        i = desc.find(' ')
        self.name = desc[0:i]
        i = desc.find('(',i+1)
        j = desc.find(')',i+1)
        self.weight = int(desc[i+1:j])
        i = desc.find('-> ', j+1)
        if i == -1:
            self.children = set()
        else:
            self.children = set(desc[i+3:].split(', '))

def programs(filename):
    with open(filename, 'r') as f:
        for l in f:
            line = l.strip()
            if line:
                yield Program(line)

def main(filename):
    candidates = []
    children = set()
    for prog in programs(filename):
        if prog.children:
            candidates.append(prog.name)
            children = children | prog.children

    for c in candidates:
        if c not in children:
            print(c)
            return

    print('Not found')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input.txt')
