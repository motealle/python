# input:
# 266 Elga Caputo 1990-05-05
# 160 Aaron Riva 1989-09-15
# 351 Demis Ferraro 1991-08-15
# 357 Nico Grassi 1995-02-09
# 336 Albino Rossi 1994-05-30
# 569 Radames Bernardi 1991-04-19
# 522 Elio Pellegrino 1994-04-26
# *
# no 357
# fn Demis
# ln Rossi
# bd 1990-05-05
# fn Nina
# *
import string
n='b'
while (n != '*'):
	n = raw_input('')
	a = n.split()
	for b in a:
		print b
    