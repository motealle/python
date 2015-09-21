import string
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

c = ' '
d = []
for i in range(0, 3):
    b.append([])
    for j in range(0, 3):
        b[i].append(' ')
tic(b)
acceptables = ['X', 'x', 'O', 'o']
while True:
    n = raw_input()
    if n == '*':
        break
    e = ['1', '1', ' ']
    if len(n.split()) == 3:
        e = (n.split())
    # print 'e is: ', e
    # print 'b is: ', b
    if e[0].isdigit() and e[1].isdigit():
        # n,m=int(e[0]-1),int(e[1])-1

        if ((len(e[2]) == 1) and (int(e[0]) in
                                  range(1, 4) and int(e[1]) in range(1, 4)) and
                b[int(e[0])-1][int(e[1])-1] == ' '):
            b[int(e[0])-1][int(e[1])-1] = e[2]
    # print 'b is: ', b
    # print range(1,4)
    # b[0][0] = 'x'
    # c = [0*10]
    # c[int(b[0])][int(b[1])] = b[2]
    # print c

    tic(b)
