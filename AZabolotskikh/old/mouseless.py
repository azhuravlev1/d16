names = open("names.txt", 'r');

dict = {}
for line in names:
	surname, name = line.split();
	surname.strip(); name.strip();
	dict[surname] = (name, None);

bdates = open("birthdates.txt", 'r');
ofile = input("Enter name of output file\n (Enter \"stdout\" to write to console)\n")
for line in bdates:
	surname, bdate = line.split();
	surname.strip(); bdate.strip();
	dict[surname] = (dict[surname][0], bdate);

iter = sorted(list(dict), key = lambda x: dict[x][0]);
if ofile != "stdout":
	ofile = open(ofile, 'w');
for surname in iter:
	if ofile == "stdout":
		print (surname, dict[surname][0], dict[surname][1], sep = '\t');
	else:
		ofile.write((surname + '\t' + dict[surname][0] + '\t' + dict[surname][1] + '\n'));
