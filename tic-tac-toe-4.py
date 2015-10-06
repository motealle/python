import string
import sys
b = []

# a = [[' '][' ']]*3
# a='b'
a = []
for i in range(8):
    a.append('')
# print range(8)


def tic(a):
    print '''    1   2   3
  +---+---+---+
1 | %s | %s | %s |
  +---+---+---+
2 | %s | %s | %s |
  +---+---+---+
3 | %s | %s | %s |
  +---+---+---+''' % ((a[0][0], a[0][1], a[0][2], a[1][0],
                       a[1][1], a[1][2], a[2][0], a[2][1], a[2][2]))
    if wincheck(a):
        sys.exit()


def wincheck(a):
    if a[0][0] == a[0][1] == a[0][2] and a[0][2] in {'X', 'O'}:
        print a[0][0], 'wins the game'
        return 1
    if a[1][0] == a[1][1] == a[1][2] and a[1][2] in {'X', 'O'}:
        print a[1][0], 'wins the game'
        return 1
    if a[2][0] == a[2][1] == a[2][2] and a[2][2] in {'X', 'O'}:
        print a[2][0], 'wins the game'
        return 1
    if a[0][0] == a[1][1] == a[2][2] and a[2][2] in {'X', 'O'}:
        print a[0][0], 'wins the game'
        return 1
    if a[0][0] == a[1][0] == a[2][0] and a[2][0] in {'X', 'O'}:
        print a[0][0], 'wins the game'
        return 1
    if a[0][1] == a[1][1] == a[2][1] and a[2][1] in {'X', 'O'}:
        print a[0][1], 'wins the game'
        return 1
    if a[0][2] == a[1][2] == a[2][2] and a[2][2] in {'X', 'O'}:
        print a[0][2], 'wins the game'
        return 1
    if a[0][2] == a[1][1] == a[2][0] and a[2][0] in {'X', 'O'}:
        print a[0][2], 'wins the game'
        return 1


c = ' '
d = []
for i in range(0, 3):
    b.append([])
    for j in range(0, 3):
        # vv = '%s%s' % (i+1 , j+1)
        b[i].append(' ')
tic(b)
status = 'X'
while True:
    err = False
    n = raw_input()
    if n == '*':
        break
    e = [' ', ' ']
    if len(n.split()) == 2:
        e = (n.split())
        for chck in (n.split()):
            if chck.isdigit() == False:
                if not err:
                    print 'invalid input'
                    err = True
    else:
        if not err:
            print 'invalid input'
            err = True

    # print 'e is: ', e
    # print 'b is: ', b
    if e[0].isdigit() and e[1].isdigit():
        # n,m=int(e[0]-1),int(e[1])-1

        if int(e[0]) in range(1, 4) and int(e[1]) in range(1, 4):
            if ((b[int(e[0])-1][int(e[1])-1] in {'X', 'O'})):
                print 'cell is already taken'
                err = True
        if (((status) == 'X') and (int(e[0]) in
           range(1, 4) and int(e[1]) in range(1, 4)) and
           b[int(e[0])-1][int(e[1])-1] == ' '):
            b[int(e[0])-1][int(e[1])-1] = 'X'
            status = 'O'
        if (int(e[0]) not in range(1, 4) or
                int(e[1]) not in range(1, 4)):
            if not err:
                print 'invalid input'
                err = True
        if (((status) == 'O') and (int(e[0]) in
           range(1, 4) and int(e[1]) in range(1, 4)) and
           b[int(e[0])-1][int(e[1])-1] == ' '):
            b[int(e[0])-1][int(e[1])-1] = 'O'
            status = 'X'
        if not err:
            tic(b)
            err = False
