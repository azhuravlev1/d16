k = 10
b = dict()
for i in range(k):
	n = dict()
	for j in range(k):
		s = dict()
		for z in range(k):
			s[z] = z
		n[j] = s
	b[i] = n
b[1][6][9] = "zzzzz"
print(b)