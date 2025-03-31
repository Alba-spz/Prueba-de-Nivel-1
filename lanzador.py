from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta

def lanzador_main(): 
    vehiculos = []

    vehiculos.append(Coche("blanco", 4, 170, 1520))
    vehiculos.append(Coche("amarillo", 4, 200, 2000))
    vehiculos.append(Bicicleta("naranja", 2, "btwin", "rockrider", "urbana"))
    vehiculos.append(Bicicleta("verde", 2, "trek", "r3", "deportiva"))
    vehiculos.append(Camioneta("gris", 4, 90, 1990, "opel", "astra", 1300))
    vehiculos.append(Motocicleta("azul",2,"Yamaha","XSR", "Deportiva", 220, 930))
    
    return vehiculos # Llamamos a la función catalogar que recibe una lista de vehículos
    
def catalogar_simple(vehiculos): # Método que recibe una lista de vehículos y las imprime
    for vehiculo in vehiculos:
        print(f"Clase: {vehiculo.__class__.__name__}")
        for atributo, valor in vehiculo.__dict__.items():
            print(f"{atributo}: {valor}")
        print()

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vf for vf in vehiculos if int(vf.ruedas) == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(f"Clase: {vehiculo.__class__.__name__}") #¿Por qué después de __name__ no se ponen paréntesis? Porque __name__ es un atributo, no un método.
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()
    else:
        for vehiculo in vehiculos:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()

def menu():
    print("Elija el tipo de vehículo que desea ver:")
    print("1. Coche")
    print("2. Bicicleta")
    print("3. Camioneta")
    print("4. Motocicleta")
    print("5. Ordenar por ruedas")
    print("6. Salir")

def obtener_datos_vehiculo(tipo):
    if tipo == 1:
        color = input("Introduce el color del coche: ")
        ruedas = input("Introduce el número de ruedas del coche: ")
        velocidad = input("Introduce la velocidad del coche: ")
        cilindrada = input("Introduce la cilindrada del coche: ")
        return Coche(color, ruedas, velocidad, cilindrada)
    
    elif tipo == 2:
        color = input("Introduce el color de la bicicleta: ")
        ruedas = input("Introduce el número de ruedas de la bicicleta: ")
        marca = input("Introduce la marca de la bicicleta: ")
        modelo = input("Introduce el modelo de la bicicleta: ")
        tipo = input("Introduce el tipo de bicicleta: ")
        return Bicicleta(color, ruedas, marca, modelo, tipo)
    
    elif tipo == 3:
        color = input("Introduce el color de la camioneta: ")
        ruedas = input("Introduce el número de ruedas de la camioneta: ")
        velocidad = input("Introduce la velocidad de la camioneta: ")
        cilindrada = input("Introduce la cilindrada de la camioneta: ")
        marca = input("Introduce la marca de la camioneta: ")
        modelo = input("Introduce el modelo de la camioneta: ")
        capacidad_carga = input("Introduce la capacidad de carga de la camioneta: ")
        return Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, capacidad_carga)
    
    elif tipo == 4:
        color = input("Introduce el color de la motocicleta: ")
        ruedas = input("Introduce el número de ruedas de la motocicleta: ")
        marca = input("Introduce la marca de la motocicleta: ")
        modelo = input("Introduce el modelo de la motocicleta: ")
        tipo = input("Introduce el tipo de motocicleta: ")
        velocidad = input("Introduce la velocidad de la motocicleta: ")
        cilindrada = input("Introduce la cilindrada de la motocicleta: ")
        return Motocicleta(color, ruedas, marca, modelo, tipo, velocidad, cilindrada)
    
    elif tipo == 5:
        ruedas = int(input("Introduce el número de ruedas por el que quieres filtrar: "))
        return ruedas
    else:
        return None
     





