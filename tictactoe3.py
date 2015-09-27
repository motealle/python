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
        # return
        break
    c = (n.split())
    finded = False
    # print c
    ff = True
    for i in range(0, len(a)):

        # if (c[0] in lst and c[1] in a[i] and ff):
        if (c[0] == 'no' and c[1] == a[i][0] and ff):
        if (c[0] == 'fn' and c[1] == a[i][1] and ff):
        if (c[0] == 'ln' and c[1] == a[i][2] and ff):
        if (c[0] == 'bd' and c[1] == a[i][3] and ff):

            ff = False
            finded = True
            print "-----------------------------------"
            if c[0] == 'no':
                print "search result for \"no %s\":" % a[i][0]
            elif c[0] == 'fn':
                print "search result for \"fn %s\":" % a[i][1]
            elif c[0] == 'ln':
                print "search result for \"ln %s\":" % a[i][2]
            elif c[0] == 'bd':
                print "search result for \"bd %s\":" % a[i][3]
            print "-----------------------------------"
            print "number: %s" % a[i][0]
            print "first name: %s" % a[i][1]
            print "last name: %s" % a[i][2]
            print "birth date: %s" % a[i][3]
            break
    if not finded:
        # if c[0] in lst and c[1] not in a[i]:
        if c[0] in lst and c[1] != a[i]:
            print "-----------------------------------"
            print "search result for \"%s %s\":" % (c[0], c[1])
            print "-----------------------------------"
            print "not found"
            break
print "-----------------------------------"
