file1 = str(input())
file2 = str(input())
dict = {"Ашихмин":"Ашихмин Иван",\
	"Байкабулов":"Байкабулов Тимур",\
	"Безель":"Безель Елизавета",\
	"Гехт":"Гехт Артём",\
	"Гунченко":"Гунченко Любовь",\
	"Журавлёв":"Журавлёв Андрей",\
	"Забазарных":"Забазарных Варвара",\
	"Заболотских":"Заболотских Александр",\
	"Злобин":"Злобин Александр",\
	"Крылов":"Крылов Дмитрий",\
	"Кудрявцев":"Кудрявцев Еремей",\
	"Кудрявцева":"Кудрявцева Полина",\
	"Машкова":"Машкова Ольга",\
	"Мурашко":"Мурашко Матвей",\
	"Рыжков":"Рыжков Кирилл",\
	"Суханов":"Суханов Григорий",\
	"Фесюк":"Фесюк Марина",\
	"Хумонен":"Хумонен Иннокентий",\
	"Шуваева":"Шуваева Елизавета"}
f_read = open(file1, 'r',encoding = 'utf8')
for line in f_read.readlines():
	line = line.strip()
	r = line.replace(dict)
f_read.close()
f_read = open(file2, 'w')
f_read.writelines(r)
f_read.close()

f_read = open(file2, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
f_read.close()