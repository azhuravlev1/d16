file1 = str(input())
file2 = str(input())
f_read = open(file1, 'r')
f_read1 = open(file2, 'w')
for line in f_read.readlines():
	line = line.strip()
	s = line.split()
	for j in s:
		f = j + '\n'
		f_read1.writelines(f)

f_read.close()
f_read1.close()

f_read = open(file2, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
f_read.close()

	
