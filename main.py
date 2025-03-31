from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from lanzador import lanzador_main, menu, obtener_datos_vehiculo, catalogar

if __name__ == "__main__": # Esto es para que no se ejecute el código si se importa este archivo desde otro
    vehiculos = lanzador_main() # Llamamos a esta función para obtener la lista de vehículos que ya existen

    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 6:
            break

        vehiculo = obtener_datos_vehiculo(opcion)

        if isinstance(vehiculo, int):
            catalogar(vehiculos, vehiculo)
        elif vehiculo:
            vehiculos.append(vehiculo)
            print(f"Vehículo añadido: {vehiculo}") 
        else:
            print("Error al añadir el vehículo, inténtelo de nuevo")

    lanzador_main() # Llamamos a la función que lanza el programa

    