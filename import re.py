from pickle import TRUE
import re


cadenaselect=(input("Ingrese la cadena que quiere para realizar la busqueda: "))
busquedaselect=(input("Ingrese la palabra que quiere buscar: "))
if re.search(busquedaselect,cadenaselect):
    print ("Palabra encontrada en la cadena")
else:
    print("No se encontró la palabra en la cadena")