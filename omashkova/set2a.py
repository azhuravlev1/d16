pairs = []
while True:
	key = input("Введите key: ")
	if key == 'end':
		break
	value = input("Введите value: ")
	pairs.append((int(key), value))	

def group_pairs(pairs):
	a = {}
	for i in pairs:
		a[i[0]] = []
	for i in pairs:
		a[i[0]].append(i[1])
	return a

print(group_pairs(pairs))
