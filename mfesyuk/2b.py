def group(pairs):
	d = {}
	for p in pairs:
		if p[0] not in d:
			d[p[0]] = [p[1]]
		else:
			d[p[0]].append(p[1]])
	return d
import sys
file_read = sys.argv[1]
file_write = sys.argv[2]
A = []
with open(file_read, 'r', encoding = "utf8") as f_read:
	for line in f_read:	
		A.append(list(map(tuple, line.split())))
A = group(A)
with open(file_write, 'w', encoding = "utf8") as f_write:
	for i in range(len(A)):
		f_write.write(A[i])
