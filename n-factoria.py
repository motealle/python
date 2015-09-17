n = input()
if (n >= 0):
    c = 1
    nf = 1
    if (n == 0 or n == 1):
        print c

    else:
        while (c < n and n != 0):
            c += 1
            nf *= c
        print nf
