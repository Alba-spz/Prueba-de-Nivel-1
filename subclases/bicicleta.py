from superclases.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, marca, modelo, tipo):
        super().__init__(color, ruedas) # Llamamos al constructor de la clase padre
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self): # Método que se ejecuta cuando se imprime el objeto
        return f"Bicicleta(color={self.color},ruedas={self.ruedas}, marca={self.marca}, modelo={self.modelo},tipo={self.tipo})"
    
    def __name__(self):
        return self.__class__.__name__() #Este método sirve para obtener el nombre de la clase de un objeto
    
    def __representacion__(self): 
        return f"{self.__class__.__name__}({self.color},{self.ruedas},{self.marca},{self.modelo},{self.tipo})" 

    def arrancar(self):
        print(f"La bicicleta {self.marca} con modelo {self.modelo} ya se puede usar para pedalear.")

    def frenar(self):
        print(f"La bicicleta {self.marca} con modelo {self.modelo} está frenando.")

    def catalogar_bicicletas(bicicletas): # Método que recibe una lista de bicicletas y las imprime
        for bicicleta in bicicletas:
            print(f"{bicicleta.__class__.__name__}: {bicicleta}")
    
    def catalogar(vehiculos): # Método que recibe una lista de vehículos y las imprime
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")