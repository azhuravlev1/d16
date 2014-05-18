f_read = open('in.txt', 'r')
f_write = open('out.txt', 'w')
for line in f_read.readlines():
	f_write.writelines(line)
f_read.close()
f_write.close()
