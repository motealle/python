inp = ''
lst = []
while True:
    inp = raw_input()
    if inp == '0':
        break
    if inp.isdigit():
        lst.append(inp)
inp = raw_input()
if inp.isdigit():
    # print lst
    if inp in lst:
        print 'yes'
    else:
        print 'no'
