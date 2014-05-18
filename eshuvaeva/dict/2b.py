name = str(input())
a = []
f_read = open(name, 'r')
for line in f_read.readlines():
	line = line.strip()
	s = line.split(" ")
	k = (s[0],s[1])
	a.append(k)
	d = dict()
	for i in range(len(a)):
		if a[i][0] not in d:
			d[a[i][0]] = a[i][1]
		else:
			d[a[i][0]]= d[a[i][0]] + ',' + a[i][1]
print(d)
f_read.close()
