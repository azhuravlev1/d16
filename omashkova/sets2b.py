in_file1 = input()
out_file1 = input()
in_file = open(in_file1, 'r')
strings = in_file.readlines()
out_file = open(out_file1, 'w')
words = []
for i in strings:
	i = i.strip()
	words.append(i.split("\t"))	
pairs = []
for i in words:
	pairs.append((i[0], i[1]))

def group_pairs(pairs):
	a = {}
	for i in pairs:
		a[i[0]] = []
	for i in pairs:
		a[i[0]].append(i[1])
	return a

names_and_nicks = group_pairs(pairs)
for i in names_and_nicks:
	out_file.write(i)
	out_file.write(": ")
	out_file.write(str(names_and_nicks[i]))
	out_file.write("\n")
in_file.close()
out_file.close()
