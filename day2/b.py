#!/usr/bin/python
FILENAME='b.txt'

def get_thing(l):
    l = sorted(l)
    ln = len(l)
    for i in xrange(0, len(l) - 1):
        a = l[i]
        for j in xrange(i + 1, len(l)):
             if l[j] % a == 0:
                 return l[j]/a
    '''Should never occur, but just in case '''             
    return None

def get_int_row(filename):
   with open(filename, 'r') as f:
       for line in f:
           l = line.strip()
           if l:
               yield [int(x) for x in l.split()]

def main():
    chksum = 0
    for r in get_int_row(FILENAME):
        a = get_thing(r)
        chksum = chksum + a

    print('The answer is: {}'.format(chksum))

if __name__ == '__main__':
    main()
