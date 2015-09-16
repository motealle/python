# while True:
inp = raw_input()
if inp.isdigit():
    n = int(inp)
    m = 0
    while (n > 0):
        m += 1
        n -= 1
        print((' ')*(n))+('*')*((m*2)-1)

    while (m > 1):
        m -= 1
        n += 1
        print((' ')*(n))+('*')*((m*2)-1)
        # else:
        #     break
