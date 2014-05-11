k = 10
b = dict()
for i in range(k):
	n = dict()
	for j in range(k):
		s = dict()
		for z in range(k):
			s[z] = z
		n[i] = s
	b[i] = n
print(b)