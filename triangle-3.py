n = input()
if (n >= 0):
    b = 1
    for a in range(1, n+1):
        print(' ')*(n-a)+('*')*((a*2)-1)
