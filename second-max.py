lst = []
while True:
    inp = raw_input()
    if inp == '0':
        break
    if inp.isdigit() and (int(inp) not in lst):
        lst.append(int(inp))
if len(lst) >= 2:
    lst.sort()
    lst.reverse()
    print lst[1]

    # print lst
# inp = ''
# lst = []
# while True:
#     inp = raw_input()
#     if inp == '0':
#         # lst.append(0)raw
#         break
#     if inp.isdigit():
#         lst.append(int(inp))
# if len(lst) >= 2:
#     lst.sort()
#     lst.reverse()
#     print lst[1]
#     # print lst
