inp = 1
lst = []
while inp > 0:
    inp = input()
    if inp <= 0:
        break
    lst.append(inp)
m, n = 0, 0
if len(lst) >= 1:
    for n in lst:
        m += n
    print m
