import string
import sys
import re


def udigit(isd):
    for x in (list(isd)):
        if x in list('-0123456789'):
            return True
    else:
        return False


def harfnadad(ish):
    for x in (list(ish)):
        if x.upper() in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'):
            return True
    else:
        return False


def neg(isneg):
    if udigit(isneg):
        if int(isneg) < 0:
            return True
        else:
            return False


def repl(n):
    d = n.split()
    # print d
    # print len(d), d[1], udigit(d[1]), len(d[2])
    if (len(d) == 3 and udigit(d[1]) and
            len(d[2]) == 1 and harfnadad(d[2])):
        # print abs(int(d[1]))
        if not neg(d[1]):
            if abs(int(d[1])) < len(d[0]):
                a = list(d[0])
                a[int(d[1])] = d[2]
                b = ''.join(a[:])
                print b
            else:
                print ''.join(d[0])
        else:
            if abs(int(d[1])) <= len(d[0]):
                a = list(d[0])
                a[int(d[1])] = d[2]
                b = ''.join(a[:])
                print b
            else:
                print ''.join(d[0])
    # elif len(d) == 3 and udigit(d[1]):
    #     print ''.join(d[0])
    # else:
        # print ''

for line in sys.stdin:
    if line != "\n":
        # print '\n\nfirst',line.split()
        if line[-1:] == "\n":
            repl(line[:-1])
        else:
            repl(line)
