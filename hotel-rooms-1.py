# input:
# +--+--+--+--+--+
# |  |  |  |  |  |
# +--+--+--+--+--+
# |  |  |  |  |  |
# +--+--+--+--+--+
# +

# output:
# 10
tedad = 0
n = 0
while (n != '+'):
    n = raw_input('')
    c = n.count('|  ')
    if c != 0:
        tedad += c
        if (n.count('|') == c):
            tedad -= 1
print tedad
