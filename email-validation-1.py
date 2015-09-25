import string
isd = []
domains = {'.com', 'org', 'net', '.COM', '.ORG', '.NET'}
ills = '~ ! # $ % ^ & * ( ) _ + = - j " ' + "'"


def check(n):
    # print ills.split()
    # print list(n)
    if '@' not in n:
        isd.append('0')
    if '@' in n:
        isd.append('1')
    if n.count('@') != 1:
        isd.append('0')
    if n[-4:] not in domains:
        isd.append('0')
    for g in list(n):
        if g in ills.split():
            isd.append('0')
    if n[0:1] == '.':
        isd.append('0')
    if n[n.find('@')-1:n.find('@')] == '.':
        isd.append('0')
    if n.count('.') > 2:
        isd.append('0')
    if not n.find('.', n.find('@')+1) > 1:
        isd.append('0')
    if '0' in isd:
        print '"%s" [no]' % n
    if '0' not in isd:
        print '"%s" [yes]' % n
while True:
    n = raw_input()
    if n == '^':
        break
    else:
        check(n)
