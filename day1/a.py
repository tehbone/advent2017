#!/usr/bin/python
FILENAME='a.txt'

def get_list(filename):
    lst = ''
    with open(filename, 'r') as f:
        lst = f.readline().strip()

    return lst

def main():
    lst = get_list(FILENAME)
    lst_len = len(lst)
    s = 0
    for i in xrange(0,lst_len-1):
        if lst[i] == lst[i+1]:
            s = s + int(lst[i])

    if lst[lst_len-1] == lst[0]:
        s = s + int(lst[lst_len-1])

    print('The answer is: {}'.format(s))

if __name__ == '__main__':
    main()
