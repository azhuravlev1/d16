def wrong_line (line):
	return line[::-1]

in_file = input()
strings = open(in_file).readlines()
all_words = []
for i in strings:
	i = i.strip()
	words = i.split()
	for j in words:
		all_words.append(j)
all_words.sort(key = wrong_line)
print(all_words)
