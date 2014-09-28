class Dragon:
	skin_colour = 'black'
	eyes_colour = 'yellow'
	power = 200
	treasures = ['rings','necklaces','emeralds','coins']
	def sleep(self):
		self.power = self.power - 50


class Dwarf:
	name = 'Thorin'
	strength = 400
	trophies = ['sword']
	def battle_a_dragon(self,d):
		if self.strength > d.power:
			for i in d.treasures:
				self.trophies.append(i)
			d.treasures = []
		if self.strength < d.power:
			for i in self.trophies:
				d.treasures.append(i)
			self.trophies = []


Thorin = Dwarf()
Kili = Dwarf()
Smaug = Dragon()
Kili.name = 'Kili'
Kili.strength = 150
Smaug.treasures = ['rings','necklaces','emeralds','coins','rubies','diamonds','sapphires','Arkenstone']
Ancalagon = Dragon()
Ancalagon.power = 600

Ancalagon.sleep()

import random
f = random.randrange(4)
if f == 0:
	Thorin.battle_a_dragon(Smaug)
print(Smaug.treasures)
print(Thorin.trophies)
if f == 1:
		Thorin.battle_a_dragon(Ancalagon)
print(Smaug.treasures)
print(Thorin.trophies)
if f == 2:
	Kili.battle_a_dragon(Smaug)
print(Smaug.treasures)
print(Kili.trophies)
if f == 3:
	Kili.battle_a_dragon(Ancalagon)
print(Ancalagon.treasures)
print(Kili.trophies)
	
