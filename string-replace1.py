import string
import sys
import re


def repl(n):
    d = n.split()
    print d
    if len(d) == 3 and d[1].isdigit() and len(d[2]) == 1:
        print abs(int(d[1]))
        if abs(int(d[1])) < len(d[0]):
            a = list(d[0])
            a[int(d[1])] = d[2]
            b = ''.join(a[:])
            return 'abs < len d[0]',b
        else:
            return 'abs not< len d[0]',d[0]
    elif len(d) == 3 and d[1].isdigit():
        return 'not accomplished',d[0]
    else:
        return 'nothing',n



for line in sys.stdin:
    if line != "\n":
        if line[-1:] == "\n":
            print repl(line[:-1])
        else:
            print repl(line)
