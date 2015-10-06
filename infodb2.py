import string
import sys
n = 'b'
db = []
# b = 0
a, c = [], []
lst = ['no', 'fn', 'ln', 'bd']


def insert(inp):
    a.append(inp.split()[1:])


def select(inp):
    c = (n.split()[1:])
    finded = False
    for i in range(0, len(a)):
        if c[0] == 'no' and c[1] == a[i][0]:
            finded = True
            print "%s %s %s %s" % (a[i][0], a[i][1], a[i][2], a[i][3])
        elif c[0] == 'fn' and c[1] == a[i][1]:
            finded = True
            print "%s %s %s %s" % (a[i][0], a[i][1], a[i][2], a[i][3])
        elif c[0] == 'ln' and c[1] == a[i][2]:
            finded = True
            print "%s %s %s %s" % (a[i][0], a[i][1], a[i][2], a[i][3])
        elif c[0] == 'bd' and c[1] == a[i][3]:
            finded = True
            print "%s %s %s %s" % (a[i][0], a[i][1], a[i][2], a[i][3])

    if not finded and c[0] in lst:
        print "not found"

while True:
    n = raw_input('')
    if n == '*':
        break
    if n.split()[0] == 'insert':
        insert(n)
    elif n.split()[0] == 'select':
        select(n)
