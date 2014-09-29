import random
class Zombie:
	speed = 100
	def make_faster(self,diff):
		self.speed += diff
	def kill_man(man,self):
		man.blood = 250
		man.alive=False
		self.speed=50
Zombie1 = Zombie()
Zombie1.speed = 200
Zombie1.make_faster(333)
print(Zombie1.speed)
class Man:
	name = "name"
	Alive = True
	blood = 1000
	def make_more_blood(self,diff):
		self.blood += diff
Alex=Man()
Alex.name="Alex"
Gareth=Man()
Gareth.name="Gareth"
#print(type(Alex))
#print(type(Man))
if random.randint(0,1)==0:
	Zombie1.kill_man(Gareth)
else:
	Zombie1.kill_man(Alex)
#print(Alex.blood)
#print(Gareth.blood)
if random.randint(0,1)==0:
	Alex.make_more_blood(535)
else:
	Gareth.make_more_blood(535)
print(Alex.blood)
print(Gareth.blood)
