#Creado por: Daniel Campos y Alejandro Madrigal
#Fecha: 26-10-2023
#Ultima modificacion: 
#Version: 3.12.0
import random

def seleccionarColor():
    try:
        print("1. Azul" + "\n" + "2. Amarillo" + "\n" + "3. Gris")
        colorSeleccionado = int(input("Seleccione el color de la herramienta: "))
        return colorSeleccionado
    except ValueError:
        print("Ingrese un entero como entrada para seleccionar.")
        return seleccionarColor()
class herramientas:
    def __init__(self):
        self.ID = 0
        self.durabilidad = 0
        self.metales = ""
        self.color = []

    def generarID(self):
        self.ID = random.randint(1, 100000)
        return self.ID

    def generarDurabilidad(self):
        self.durabilidad = random.randint(1, 100)
        return self.durabilidad

    def generarMetales(self):
        self.metales = random.choice(["Hierro", "Oro", "Diamante"])
        return self.metales

    def generarColor(self):
        colorSeleccionado = seleccionarColor()
        colores = ["azul", "amarillo", "gris"]
        self.color = colores[colorSeleccionado - 1]
        return self.color 
class armas(herramientas):
    def __init__(self):
        super().__init__()
        self.danno = 0
        self.velocidadAtaque = 0.0

    def generarDanno(self):
        self.danno = random.choice([7, 8, 9])
        return self.danno

    def generarVelocidadAtaque(self):
        self.velocidadAtaque = random.choice([0.1, 0.2, 0.3])
        return self.velocidadAtaque
class armaduras(herramientas):
    def __init__(self):
        super().__init__()
        self.defensa = 0

    def generarDefensa(self):
        self.defensa = random.choice([4, 5, 6])
        return self.defensa