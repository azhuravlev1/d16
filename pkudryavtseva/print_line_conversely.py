def key(a):
	a1 = a[::-1]
	return a1
f_read = open('in.txt', 'r')
for line in f_read.readlines():
	line = key(str(line))
	print(str(line))
