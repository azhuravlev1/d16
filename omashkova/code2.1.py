in_file = input()
out_file1 = input()
strings = open(in_file).readlines()
out_file = open(out_file1, 'w')
for i in strings:
	out_file.write(i)
open(in_file).close()
out_file.close()
