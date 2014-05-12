a = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'd'), (3, 'eeeee')]
dictionary = dict()
for i in range(len(a)):
	if a[i][0] not in dictionary:
		dictionary[a[i][0]] = []
	dictionary[a[i][0]].append(a[i][1])
print(dictionary)
