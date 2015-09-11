n = int(raw_input())
m=1
while  (n > 0):
    print ((' ')*(n))+('*')*((m*2)-1)
    n-=1
    m+=1

while  (m > 0):
    print ((' ')*(n))+('*')*((m*2)-1)
    m-=1
    n+=1
