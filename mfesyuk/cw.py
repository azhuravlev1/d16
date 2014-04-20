names = open("names.txt", 'r')
dict = {}
for line in names:
	surname, name = line.split()
	surname.strip()
	name.strip()
	dict[surname] = (name, None)
birth = open("birthdates.txt", 'r')
output = input("Enter name of output file\n (Enter \"stdout\" to write to console)\n")
for line in birth:
	surname, data = line.split()
	surname.strip()
	data.strip()
	dict[surname] = (dict[surname][0], data)
iter = sorted(list(dict), key = lambda x: dict[x][0])
if output != "stdout":
	output = open(output, 'w')
for surname in iter:
	if output == "stdout":
		print (surname, dict[surname][0], dict[surname][1], sep = '\t')
	else:
		output.write((surname + '\t' + dict[surname][0] + '\t' + dict[surname][1] + '\n'))
