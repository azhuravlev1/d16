in_file = input()
strings = open(in_file).readlines()
words = []
for i in strings:
	line = i.split()
	words += line
def length(j):
	return len(j)
words.sort(key = length)
print(words)
