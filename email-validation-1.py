import string
import sys
domains = {'.com', '.org', '.net', '.COM', '.ORG', '.NET'}
ills = '~ ! # $ % ^ & * ( ) _ + = - " / \\ | ? > < ` [ ] { } : ' + "'"


def check(n):
    # print ills.split()
    # print list(n)
    isd = []
    if '@' not in n:
        isd.append('0')
        # print "if '@' not in n"
    if '@' in n:
        isd.append('1')
    if n.count('@') != 1:
        isd.append('0')
        # print "if n.count('@') != 1:"
    if n[-4:] not in domains:
        isd.append('0')
        # print "if n[-4:] not in domains:"
    for g in list(n):
        if g in ills.split():
            isd.append('0')
            # print "for g in list(n):if g in ills.split():" ,g
    if n[0:1] == '.':
        isd.append('0')
        # print "if n[0:1] == '.':"
    if n[n.find('@')-1:n.find('@')] == '.':
        isd.append('0')
        # print "if n[n.find('@')-1:n.find('@')] == '.':"
    if n.count('.') > 2:
        isd.append('0')
        # print n.count('.')
    if not n.find('.', n.find('@')+1) > 1:
        isd.append('0')
        # print "if not n.find('.', n.find('@')+1) > 1:"
    if ((n.split('@')[1]).count('.')) > 1:
        # print "After @ is %d dots "% ((n.split('@')[1]).count('.'))
        isd.append('0')
    if '0' in isd:
        print '"%s" [no]' % n
    if '0' not in isd:
        print '"%s" [yes]' % n
# while True:
#     n = raw_input()
#     if n == '^':
#         break
#     else:
for line in sys.stdin:
    if line != "\n":
        if line[-1:] == "\n":
            check(line[:-1])
        else:
            check(line)
            sys.exit()
    else:
        sys.exit()