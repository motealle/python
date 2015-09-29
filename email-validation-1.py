import string
import sys
domains = {'.com', '.org', '.net', '.COM', '.ORG', '.NET'}
# ills = '~ ! # $ % ^ & * ( ) _ + = - " / \\ | ? > < ` [ ] { } : ' + "'"
alphas = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.@'
als = list(alphas)


def check(n):
    # print ills.split()
    # print list(n)
    isd = ['1']
    if len(n) < 7:
        isd.append('0')
    else:
        for v in list(n):
            if v.capitalize() not in als:
                isd.append('0')
        if n[-4:] not in domains or n[0:1] == '.' or n.count('.') > 2:
            isd.append('0')
            # print "if n[-4:] not in domains:"
        if '@' not in n:
            isd.append('0')
            # print "if '@' not in n"
        else:
            # isd.append('1')
            if n.count('@') != 1:
                isd.append('0')
            else:
                if n[n.find('@')-1:n.find('@')] == '.':
                    isd.append('0')
                if ((n.split('@')[1]).count('.')) > 1:
                    # print "After @ is %d dots "%
                    # ((n.split('@')[1]).count('.'))
                    isd.append('0')
                if n[0:1] == '@' or n[-5:-4] == '@':
                    isd.append('0')
                if not n.find('.', n.find('@')+1) > 1:
                    isd.append('0')

            # print "an illegal char is inside: %s" % v

    if '0' in isd:
        print '"%s" [no]' % n
    else:
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
    #         sys.exit()
    # else:
    #     sys.exit()
