f_read = open('in.txt', 'r')
f_write = open('out.txt', 'w')
for line in f_read.readlines():
	line = line.strip().split()
	for word in line:
		writing = word + '\n'
		f_write.writelines(writing)
f_read.close()
f_write.close()
