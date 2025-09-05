# main.py
from gestor import GestorViajes

def menu():
    gestor = GestorViajes()

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar viaje")
        print("2. Mostrar viajes")
        print("3. Mostrar resumen")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ruta = input("Ingresa la ruta: ")
            costo = float(input("Ingresa el costo ($): "))
            tiempo = int(input("Ingresa el tiempo (minutos): "))
            gestor.agregar_viaje(ruta, costo, tiempo)

        elif opcion == "2":
            gestor.mostrar_viajes()

        elif opcion == "3":
            gestor.resumen()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
