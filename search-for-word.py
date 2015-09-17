import string
inp = ''
lst = []
inp = raw_input()
lst = inp.split()
inp = raw_input()
if inp in lst:
    print 'yes'
else:
    print 'no'
