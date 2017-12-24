#!/usr/bin/python
from collections import defaultdict
import sys

class CPU(object):
    def __init__(self):
        super(CPU, self).__init__()
        self.regs = defaultdict(int)
        self.hwm = 0

    def execute(self, instr):
        parts = instr.split()
        v = parts[0]
        op = parts[1]
        arg = int(parts[2])
        cv = self.regs[parts[4]]
        cop = parts[5]
        carg = int(parts[6])

        if (cop == '>' and cv > carg or
            cop == '<' and cv < carg or
            cop == '>=' and cv >= carg or
            cop == '==' and cv == carg or
            cop == '<=' and cv <= carg or
            cop == '!=' and cv != carg):
            if op == 'inc':
                self.regs[v] = self.regs[v] + arg
            else:
                self.regs[v] = self.regs[v] - arg
            if self.regs[v] > self.hwm:
                self.hwm = self.regs[v]

def instructions(filename):
    with open(filename, 'r') as f:
        for l in f:
            line = l.strip()
            if line:
                yield line

def main(filename):
    cpu = CPU()
    for instr in instructions(filename):
        cpu.execute(instr)

    print('Largest value: {}'.format(cpu.hwm))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input.txt')
