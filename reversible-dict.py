import string
inp = ''
lst = []
while True:
    inp = str(raw_input())
    if inp == '*':
        break
    lst.append(inp)
for p in lst:
    if p[::-1] in lst:
        print p, p[::-1]
    else:
    	print p
