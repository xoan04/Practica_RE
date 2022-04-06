import re
import os
def borrarPantalla(): return os.system("cls")
def busqueda (cadena,busqueda):
    if re.search(busqueda,cadena) is not None:
        return print ("He encantrado el texto en: " +str((re.search(busqueda,cadena))))


if __name__ == "__main__":
    sw=0
    mainlist=[]
    while sw == 0:
        cadenas = int(input("Ingrese la cantidad de cadenas que desea evaluar: "))
        if cadenas > 0:
            for i in range(cadenas):
                cadena = input("ingrese su cadena número "+str(i+1)+": ")
                list(cadena)
                mainlist.append(cadena)
            
            cadenaselect=int(input("Ingrese la cadena que quiere para realizar la busqueda: "))
            busquedaselect=str(input("Ingrese la palabra que quiere buscar "))
            busqueda(cadenaselect,busquedaselect)

            break
        else:
            print("INGRESE UNA CANTIDAD VÁLIDA.")
            os.system("PAUSE")
            borrarPantalla()