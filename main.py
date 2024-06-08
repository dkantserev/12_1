class Transport:

	def __init__(self, name, max_speed, mileage):
	  	self.name = name
	  	self.max_speed = max_speed
	  	self.mileage = mileage

class Autobus(Transport):
	def toString(self):
		print(f'Название автомобиля :{self.name} скорость :{self.max_speed} пробег :{self.mileage}')
	
s=Autobus('Renaul logan',180,12)
s.toString()
