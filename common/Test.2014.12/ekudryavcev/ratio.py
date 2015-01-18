from decimal import *
getcontext().prec = 1200
class Ratio:
	def __init__(self , numer , denom=1):
		self.num = Decimal(numer)
		self.den = Decimal(denom)
	def __str__(self):
		return(str(self.num) + "/" + str(self.den))
	def __add__(self , other):
		if self.num == 0:
			return(other)
		if other.num == 0:
			return(self)
		else:
			neuden = self.den * other.den
			neunum1 = self.num * other.den
			neunum2 = self.den * other.num
			return(Ratio((neunum1 + neunum2) / neuden))
	def __mul__(self , other):
		return(Ratio(self.num * other.num , self.den * other.den))
s = Ratio(0 , 1)
def factorielle(x):
	if x:
		return(Decimal(x * factorielle(x-1)))
	else:
		return(1)
for i in range(600):
	s += Ratio(1 , factorielle(i))
print((s.num/s.den) > 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354)