#!/usr/bin/python
import sys

class InvalidWeightError(Exception):
    def __init__(self, needed, actual):
        super(InvalidWeightError, self).__init__()
        self.needed = needed
        self.actual = actual

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

    def get_weight(self, cache):
        if self.children:
            w = [(c, c.get_weight(cache)) 
                 for c in [cache[x] for x in self.children]]
            w0 = w[0][1]
            p0 = w[0][0]
            a = 1
            b = 0
            for i in xrange(1, len(w)):
                if w[i][1] == w0:
                    a = a + 1
                else:
                    w1 = w[i][1]
                    p1 = w[i][0]
                    b = b + 1
            if len(w) == a:
                return a * w0 + self.weight
            elif a == 1:
                raise InvalidWeightError(w1 - w0 + p0.weight, p0.weight)
            else:
                raise InvalidWeightError(w0 - w1 + p1.weight, p1.weight)
        else:
            return self.weight
        
def programs(filename):
    with open(filename, 'r') as f:
        for l in f:
            line = l.strip()
            if line:
                yield Program(line)

def main(filename):
    cache = {}
    candidates = []
    children = set()
    for prog in programs(filename):
        cache[prog.name] = prog
        if prog.children:
            candidates.append(prog.name)
            children = children | prog.children

    for c in candidates:
        if c not in children:
            root = cache[c]
            break

    try:
        root.get_weight(cache)
    except InvalidWeightError as e:
        print('Got {} needed {}'.format(e.actual, e.needed))
    else:
        print('Did not find error')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input.txt')
