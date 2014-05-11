a = [(1,'a'),(2,'b'),(3,'c'), (3,'e'),(2,'d')]
d = dict()
for i in range(len(a)):
	if a[i][0] not in d:
		d[a[i][0]] = a[i][1]
	else:
		d[a[i][0]]= d[a[i][0]] + ',' + a[i][1]
print(d)
