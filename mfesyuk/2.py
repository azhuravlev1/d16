import sys
file_read = sys.argv[1]
file_write = sys.argv[2]
with open(file_read, 'r', encoding = "utf8") as f_read:
	with open(file_write, 'r', encoding = "utf8") as f_write:
	for line in f_read:	
		f_write.write(line)
