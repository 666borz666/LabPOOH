#Creado por: Daniel Campos y Alejandro Madrigal
#Fecha: 26-10-2023
#Ultima modificacion: 
#Version: 3.12.0
import pickle

def graba(archivo, objetos):
    try:
        with open(archivo, "wb") as f:
            pickle.dump(objetos, f)
    except Exception as e:
        print("Error al grabar el archivo:", e)

def lee(archivo):
    try:
        with open(archivo, "rb") as f:
            objetos = pickle.load(f)
        return objetos
    except Exception as e:
        print("Error al leer el archivo:", e)
        return None