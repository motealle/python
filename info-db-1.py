# input:
# 266 Elga Caputo 1990-05-05
# 160 Aaron Riva 1989-09-15
# 351 Demis Ferraro 1991-08-15
# 357 Nico Grassi 1995-02-09
# 336 Albino Rossi 1994-05-30
# 569 Radames Bernardi 1991-04-19
# 522 Elio Pellegrino 1994-04-26
# *
# no 357
# fn Demis
# ln Rossi
# bd 1990-05-05
# fn Nina
# *
import string
n = 'b'
db = []
b = 0
a, c = [], []
lst = ['no', 'fn', 'ln', 'bd']
while 1:
    n = raw_input('')
    if n == '*':
        break
    a.append(n.split())
    b += 1
    # print a
while 1:
    n = raw_input('')
    if n == '*':
        break
    c = (n.split())
    # print c
    if c[0] in lst:
        # print 'command recogized'
        for i in range(0, len(a)):
            if c[1] in a[i]:
                # print a[i]
                out = ''
                for j in range(0, len(a[i])):
                    out += a[i][j]+' '
                print out  # len(a[i])
