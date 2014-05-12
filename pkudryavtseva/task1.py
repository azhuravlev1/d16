k = 10
d = dict()
for i in range(k):
	d[i] = i
print(d)

m = dict()
for i in range(k):
	h = dict()
	for l in range(k):
		h[l] = l
	m[i] = h
print(m)

m1 = dict()
for i in range(k):
	h1 = dict()
	for l in range(k):
		p = dict()
		for n in range(k):
			p[n] = n
		h1[l] = p
	m1[i] = h1

m1[1][9][2] = "ZZZZZZ"
print(m1)
