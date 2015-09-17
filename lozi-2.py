# while True:
inp = raw_input()
if inp.isdigit():
    n = int(inp)
    strt = n
    m = 0
    while (n > 0):
        m += 1
        n -= 1
        if n == (strt - 1):
            print((' ')*(n))+('*')+(' ')*((m*2)-3)
        else:
            print((' ')*(n))+('*')+(' ')*((m*2)-3)+('*')

    while (m > 1):
        m -= 1
        n += 1
        if n == (strt - 1):
            print((' ')*(n))+('*')+(' ')*((m*2)-3)
        else:
            # print((' ')*(n))+('*')*((m*2)-1)
            print((' ')*(n))+('*')+(' ')*((m*2)-3)+('*')
        # else:
        #     break
