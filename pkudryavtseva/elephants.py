dictionary = dict()
a = []
f_read = open('in.txt', 'r')
f_write = open('out.txt', 'w')
for line in f_read.readlines():
    line = line.strip().split()
    if line[0] not in dictionary:
        dictionary[line[0]] = line[1]
        a.append(line[0])
    else:
        dictionary[line[0]]= dictionary[line[0]] + ',' + line[1]
for i in range(len(a)):
	line = str(a[i]+':'+dictionary[a[i]]+'\n')
	f_write.writelines(line)
f_read.close()
f_write.close()
