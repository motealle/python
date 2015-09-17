import string
inp=''
dic = {}
while True:
    inp = raw_input()
    if inp == '*':
    	break
    dic[inp]=inp[::-1]
for p in dic:
	print p, dic[p]