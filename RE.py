import re
import os
def borrarPantalla(): return os.system("cls")
def busqueda (cadenapos,busqueda):
    cadenapos=mainlist[i]
    for element in cadenapos:
        if re.search(busqueda,cadenapos) is not None:
            return print ("He encantrado el texto en: " +str((re.search(busqueda,cadenapos))))


def menu():
    sw = 1
    while sw == 1:
        def borrarPantalla(): return os.system("cls")
        opcion = int(input("""
    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Ingresar Cadenas
        2 - Mostrar Cadenas
        3 - Evaluar Cadenas

    Opción: """))
        borrarPantalla()
        if opcion == 0:
            print("SALIDA EXITOSA ;)")
            sw = 0
        elif opcion == 1:
            cadenas = int(input("Ingrese la cantidad de cadenas que desea evaluar: "))
            if cadenas > 0:
                for i in range(cadenas):
                    cadena = input("ingrese su cadena número "+str(i+1)+": ")
                    list(cadena)
                    mainlist.append(cadena)
        elif opcion == 2:
            print(*mainlist)
        elif opcion == 3:
            cadenaselect=int(input("Ingrese la cadena que quiere para realizar la busqueda: "))
            busquedaselect=str(input("Ingrese la palabra que quiere buscar "))
            busqueda(ca)
        


if __name__ == "__main__":
    sw=0
    mainlist=[]
    cadenaselect=
    busquedaselect=""