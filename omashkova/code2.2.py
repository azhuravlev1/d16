in_file = input()
out_file1 = input()
strings = open(in_file).readlines()
out_file = open(out_file1, 'w')
for i in strings:
	words = i.split()
	for j in words:
		out_file.write(j)
		out_file.write('\n')
open(in_file).close()
out_file.close()
