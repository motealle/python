import string
inp = ''
lst = []
while True:
    inp = raw_input()
    pin = inp[::-1]
    if (inp == '*'):
        break
    if inp == pin:
        print 'yes'
    else:
        print 'no'
