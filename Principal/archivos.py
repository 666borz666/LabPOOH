#Creado por: Daniel Campos y Alejandro Madrigal
#Fecha: 26-10-2023
#Ultima modificacion: 
#Version: 3.12.0
import pickle

def graba(archivo, objeto):
    try:
        f = open(archivo, "wb")
        pickle.dump(objeto, f)
        f.close()
    except:
        print("Error al grabar el archivo")
    return

def lee(archivo):
    try:
        f = open(archivo, "rb")
        objeto = pickle.load(f)
        f.close()
    except:
        objeto = None
    return objeto