#!/usr/bin/python
import sys

def get_offsets():
    with open('input.txt', 'r') as f:
        for line in f:
            l = line.strip()
            if l:
                yield l

def get_instr():
    return [ int(x) for x in get_offsets() ]

def main(instr):
    steps = 0
    i = 0
    num_instr = len(instr)
    while True:
        offset = instr[i]
        j = offset + i
        instr[i] = instr[i] + (1 if offset < 3 else -1)
        steps = steps + 1
        if j < 0 or j >= num_instr:
            break
        i = j

    print('Num steps: {}'.format(steps))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main([int(x) for x in sys.argv[1::]])
    else:
        main(get_instr())
