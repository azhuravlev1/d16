file1 = str(input())
file2 = str(input())
d = dict()
a = []
f_read = open(file1, 'r')
f_read1 = open(file2, 'w')
for line in f_read.readlines():
	line = line.strip()
	for j in range(len(line)):
		if line[j][0] not in d:
			d[line[j][0]] = line[1]
		else:
			d[line[j][0]]= d[line[j][0]] + ',' + line[1]
	print(d)
f_read.close()
f_read1.close()
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	#print(line)
f_read.close()
