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
        if c[0] in lst and c[1] == a[i][lst.index(c[0])]:
            finded = True
            print "%s %s %s %s" % (a[i][0], a[i][1], a[i][2], a[i][3])
            # print (a[i][z] for z in range(3))
    if not finded and c[0] in lst:
        print "not found"


def update(inp):
    c = (n.split()[1:])
    finded = False
    for i in range(0, len(a)):
        if c[0] in lst and c[1] == a[i][lst.index(c[0])]:
            finded = True
            a[i][lst.index(c[-2])] = c[-1]
    if not finded and c[0] in lst:
        return 0


while True:
    n = raw_input('')
    if n == '*':
        break
    if n.split()[0] == 'insert':
        insert(n)
    elif n.split()[0] == 'select':
        select(n)
    elif n.split()[0] == 'update' and len(n.split()) == 6:
        if (n.split()[1] in lst and n.split()[3] == 'set' and
           n.split()[4] in lst):
            update(n)
