class Vehiculo():
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def __str__(self):
		return "Color {}, {} ruedas".format(self.color, self.ruedas)
	
	def __name__(self):
		return self.__class__.__name__ # __class__ es un atributo que contiene la clase de un objeto y __name__ es un atributo que contiene el nombre de la clase de un objeto.
	
	def catalogar(vehiculos):
		for vehiculo in vehiculos:
			print(type(vehiculo).__name__, vehiculo)