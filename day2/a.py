#!/usr/bin/python
FILENAME='a.txt'

def get_minmax(l):
    a = l[0]
    b = l[0]
    for i in xrange(1, len(l)):
        if l[i] < a:
            a = l[i]
        elif l[i] > b:
            b = l[i]

    return a, b

def get_int_row(filename):
   with open(filename, 'r') as f:
       for line in f:
           l = line.strip()
           if l:
               yield [int(x) for x in l.split()]

def main():
    chksum = 0
    for r in get_int_row(FILENAME):
        a, b = get_minmax(r)
        chksum = chksum + b - a

    print('The answer is: {}'.format(chksum))

if __name__ == '__main__':
    main()
