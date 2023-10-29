#Creado por: Daniel Campos y Alejandro Madrigal
#Fecha: 26-10-2023
#Ultima modificacion: 
#Version: 3.12.0
import clases
import archivos

equipos = []

def registrarArma():
    arma = clases.armas()
    arma.generarID()
    arma.generarDurabilidad()
    arma.generarMetales()
    arma.generarDanno()
    arma.generarVelocidadAtaque()
    arma.generarColor()
    equipos.append(arma)
    archivos.graba("armas.txt", equipos)
    return
def registrarArmadura():
    armadura = clases.armaduras()
    armadura.generarID()
    armadura.generarDurabilidad()
    armadura.generarMetales()
    armadura.generarDefensa()
    armadura.generarColor()
    equipos.append(armadura)
    archivos.graba("armaduras.txt", armadura)
    return
def desgastarArma():
    armas = archivos.lee("armas.txt")
    if armas is None:
        print("No hay armas registradas.")
        return
    print("Armas registradas:")
    for i, arma in enumerate(armas):
        print(f"{i + 1}. ID: {arma.ID}, Durabilidad: {arma.durabilidad}")
    try:
        opcion = int(input("Ingrese el número de arma que desea desgastar (o 0 para cancelar): "))
        if opcion == 0:
            return
        elif opcion > 0 and opcion <= len(armas):
            arma = armas[opcion - 1]
            if arma.durabilidad <= 0:
                print(f"El arma {arma.ID} ya está desgastada y se eliminará.")
                armas.pop(opcion - 1)  # Eliminar el arma de la lista
            else:
                print("¿Desgastar arma?")
                print("1. Si")
                print("2. No")
                opcion = int(input("Ingrese la opción: "))
                if opcion == 1:
                    arma.durabilidad -= 25
                    if arma.durabilidad <= 0:
                        print(f"El arma {arma.ID} se ha desgastado por completo y se eliminará.")
                        armas.pop(opcion - 1)  # Eliminar el arma de la lista
                    else:
                        print(f"La durabilidad del arma {arma.ID} es ahora: {arma.durabilidad}")
                elif opcion == 2:
                    print("No se desgastó el arma.")
                else:
                    print("Ingrese una opción válida.")
        else:
            print("Número de arma no válido.")
    except ValueError:
        print("Ingrese un número válido.")
    archivos.graba("armas.txt", armas)
def eliminarEquipo():
    try:
        print("¿Qué equipo desea eliminar?")
        print("1. Arma\n2. Armadura")
        opcion = int(input("Ingrese la opción: "))   
        if opcion == 1:
            armas = archivos.lee("armas.txt")
            idSeleccionada = int(input("Ingrese el ID del arma: "))
            for arma in armas:
                if idSeleccionada == arma.ID:
                    armas.remove(arma)
                    print("El arma se ha eliminado.")
                    equipos.append(armas)
                    archivos.graba("armas.txt", equipos)
                    return
            print("El ID ingresado no existe.")
            return eliminarEquipo()
    except ValueError:
        print("Ingrese un entero como entrada para seleccionar.")
        return eliminarEquipo()
def mostrarHerramientas():
    try:
        print("¿Que herramientas desea mostrar?")
        print("1. Armas" + "\n" + "2. Armaduras" + "\n" + "3. Todas")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            armas = archivos.lee("armas.txt")
            if armas == None:
                print("No hay armas registradas.")
            else:
                for arma in armas:
                    print("***********************************************")
                    print("ID: " + str(arma.ID))
                    print("Durabilidad: " + str(arma.durabilidad))
                    print("Metal: " + arma.metales)
                    print("Daño: " + str(arma.danno))
                    print("Velocidad de ataque: " + str(arma.velocidadAtaque))
                    print("Color: " + arma.color)
                    print("***********************************************")
                return
        elif opcion == 2:
            armaduras = archivos.lee("armaduras.txt")
            if armaduras == None:
                print("No hay armaduras registradas.")
            else:
                for armadura in armaduras:
                    print("***********************************************")
                    print("ID: " + str(armadura.ID))
                    print("Durabilidad: " + str(armadura.durabilidad))
                    print("Metal: " + armadura.metales)
                    print("Defensa: " + str(armadura.defensa))
                    print("Color: " + armadura.color)
                    print("***********************************************")
                return
        elif opcion == 3:
            armas = archivos.lee("armas.txt")
            if armas == None:
                print("No hay armas registradas.")
            else:
                for arma in armas:
                    print("***********************************************")
                    print("ID: " + str(arma.ID))
                    print("Durabilidad: " + str(arma.durabilidad))
                    print("Metal: " + arma.metales)
                    print("Daño: " + str(arma.danno))
                    print("Velocidad de ataque: " + str(arma.velocidadAtaque))
                    print("Color: " + arma.color)
                    print("***********************************************")
                return
            armaduras = archivos.lee("armaduras.txt")
            if armaduras == None:
                print("No hay armaduras registradas.")
            else:
                for armadura in armaduras:
                    print("***********************************************")
                    print("ID: " + str(armadura.ID))
                    print("Durabilidad: " + str(armadura.durabilidad))
                    print("Metal: " + armadura.metales)
                    print("Defensa: " + str(armadura.defensa))
                    print("Color: " + armadura.color)
                    print("***********************************************")
                return
        else:
            print("Ingrese una opcion valida.")
            return mostrarHerramientas()
    except ValueError:
        print("Ingrese un entero como entrada para seleccionar.")
        return mostrarHerramientas()
def mostrarArmasMetal():
    try:
        armas = archivos.lee("armas.txt")
        print("Seleccione el metal de las armas que desea mostrar.")
        print("1. Hierro" + "\n" + "2. Oro" + "\n" + "3. Diamante")
        opcion = int(input("Ingrese la opcion: "))
        try:
            if opcion == 1:
                for arma in armas:
                    if arma.metales == "Hierro":
                        print("***********************************************")
                        print("ID: " + str(arma.ID))
                        print("Durabilidad: " + str(arma.durabilidad))
                        print("Metal: " + arma.metales)
                        print("Daño: " + str(arma.danno))
                        print("Velocidad de ataque: " + str(arma.velocidadAtaque))
                        print("Color: " + arma.color)
                        print("***********************************************")
                        return
            elif opcion == 2:
                for arma in armas:
                    if arma.metales == "Oro":
                        print("***********************************************")
                        print("ID: " + str(arma.ID))
                        print("Durabilidad: " + str(arma.durabilidad))
                        print("Metal: " + arma.metales)
                        print("Daño: " + str(arma.danno))
                        print("Velocidad de ataque: " + str(arma.velocidadAtaque))
                        print("Color: " + arma.color)
                        print("***********************************************")
                        return
            elif opcion == 3:
                for arma in armas:
                    if arma.metales == "Diamante":
                        print("***********************************************")
                        print("ID: " + str(arma.ID))
                        print("Durabilidad: " + str(arma.durabilidad))
                        print("Metal: " + arma.metales)
                        print("Daño: " + str(arma.danno))
                        print("Velocidad de ataque: " + str(arma.velocidadAtaque))
                        print("Color: " + arma.color)
                        print("***********************************************")
                        return
        except ValueError:
            print("Ingrese un entero como entrada para seleccionar.")
            return mostrarArmasMetal()
    except ValueError:
        print("Ingrese un entero como entrada para seleccionar.")
        return mostrarArmasMetal()