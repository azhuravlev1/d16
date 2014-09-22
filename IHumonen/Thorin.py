class Orc:
	def __init__(self):
		self.anger = 1
		self.strenght = 1
		self.size = 100
	def rage(self):
		self.anger = 100
	def power(self):
		self.strenght=self.strenght*self.anger+size
		print('your power= ', self.strenght)
		return self.strenght
	def eat(self, meat):
		self.size+=meat
		print('gryshnak pokushal')

gryshnak=Orc()
meat=10
#Thorin Oakenshield Eikinskjaldi
#gnome
class gnome_hero:
	def __init__(self):
		self.strenght=10000
	def say(self):
		print('Ya Thorin, syn Thraina, syna Throra!')
		self.strenght+=10
	def power(self):
		return self.strenght
def  battle(x, y):
	x.eat(meat)
	y.say()
	x.rage()
	if gryshnak.strenght > Thorin_Eikinskjaldi.strenght:
		print('gryshnak win')
	else:
		print('Thorin_Eikinskjaldi win')
			
Thorin_Eikinskjaldi=gnome_hero()
battle(gryshnak, Thorin_Eikinskjaldi)
#gryshnak