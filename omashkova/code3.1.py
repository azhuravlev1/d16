in_file = input()
strings = open(in_file).readlines()
words = []
for i in strings:
	line = i.split()
	words += line
words.sort()
print(words)
