#!/usr/bin/python
import sys

IN_GROUP=1
IN_GARBAGE=2

class Group(object):
    def __init__(self, score):
        super(Group, self).__init__()
        self.score = score

def stream(filename):
    with open(filename, 'r') as f:
        while True:
            ch = f.read(1)
            if ch:
                yield ch
            else:
                break

def main(filename):
    groups = []
    s = 0
    state = IN_GROUP 
    for ch in stream(filename):
        if state == IN_GROUP:
            if ch == '{':
                s = s + 1
            elif ch == '}':
                groups.append(Group(s))
                s = s - 1
            elif ch == '<':
                state = IN_GARBAGE
                escape = False
        elif state == IN_GARBAGE:
            if escape:
                escape = False
            elif ch == '!':
                escape = True
            elif ch == '>':
                state = IN_GROUP
    print('Score: {}'.format(sum([x.score for x in groups])))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input.txt')
