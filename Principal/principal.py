#Creado por: Daniel Campos y Alejandro Madrigal
#Fecha: 26-10-2023
#Ultima modificacion: 
#Version: 3.12.0
import funciones

def menu():
    try:
        print("1. Registrar arma")
        print("2. Registrar armadura")
        print("3. Desgastar arma")
        print("4. Eliminar equipo")
        print("5. Mostrar herramientas")
        print("6. Mostrar armas de metal")
        print("7. Salir")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            funciones.registrarArma()
            return menu()
        elif opcion == 2:
            funciones.registrarArmadura()
            return menu()
        elif opcion == 3:
            funciones.desgastarArma()
            return menu()
        elif opcion == 4:
            funciones.eliminarEquipo()
            return menu()
        elif opcion == 5:
            funciones.mostrarHerramientas()
            return menu()
        elif opcion == 6:
            funciones.mostrarArmasMetal()
            return menu()
        elif opcion == 7:
            return
    except ValueError:
        print("Ingrese una entero como entrada para seleccionar.")
        return menu()