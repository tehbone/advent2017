#!/usr/bin/python
FILENAME='b.txt'

def get_list(filename):
    lst = ''
    with open(filename, 'r') as f:
        lst = f.readline().strip()

    return lst

def main():
    lst = get_list(FILENAME)
    lst_len = len(lst)
    cmp_dist = lst_len / 2
    s = 0
    for i in xrange(0,lst_len):
        j = (i + cmp_dist) % lst_len
        if lst[i] == lst[j]:
            s = s + int(lst[i])

    print('The answer is: {}'.format(s))

if __name__ == '__main__':
    main()
