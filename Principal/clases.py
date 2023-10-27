#Creado por: Daniel Campos y Alejandro Madrigal
#Fecha: 26-10-2023
#Ultima modificacion: 
#Version: 3.12.0
import random

class herramientas:
    def __init__(self):
        self.ID = 0
        self.durabilidad = 0
        self.metales = ""
        self.color = 0
        
    def ID(self):
        self.ID = random.randint(1,100000)
        print(self.ID)
        return self.ID
    
    def durabilidad(self):
        self.durabilidad = random.randint(1,100)
        return self.durabilidad
    
    def metales(self):
        self.metales = ["oro","hierro","diamante"]
        return self.metales
    
    def color(self):
        self.color = ["azul","amarillo","gris"]
        return self.color
    
class armas(herramientas):
    def __init__(self):
        self.danno = 0
        self.velocidadAtaque = 0
        
    def danno(self):
        self.danno = [7,8,9]
        return self.danno
    
    def velocidadAtaque(self):
        self.velocidadAtaque = [0.1, 0.2, 0.3]
        return self.velocidadAtaque

class armaduras(herramientas):
    def __init__(self):
        self.defensa = 0

    def defensa(self):
        self.defensa = [4,5,6]
        return self.defensa