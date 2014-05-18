a = []
def key(a):
	return len(a)
f_read = open('in.txt', 'r')
for line in f_read.readlines():
	line = line.strip().split()
	for word in line:
		a.append(word)
f_read.close()
a = sorted(a, key = key)
for i in range(len(a)):
	print(str(a[i]), end = ' ')
