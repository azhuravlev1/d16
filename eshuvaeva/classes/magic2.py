
class Vector:
	coord = []
	def __add__(self, other):
		one = self.coord[0]+other.coord[0]
		two = self.coord[1]+other.coord[1]
		s = [one, two]
		return s
v1 = Vector()
v2 = Vector()
v1.coord = list(map(int, input().split()))
v2.coord = list(map(int, input().split()))
v3 = v1+v2
print(v3)



