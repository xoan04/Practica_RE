import re 
  
expression = re.compile(r"[A-Z][A-Z][A-Z]\d\d\d\d[a-z][a-z][a-z](@hotmail.com)[^a-zA-Z0-9@][^a-zA-Z0-9@][^a-zA-Z0-9@][@]$")
pASS=input("Ingrese una contraseña: ")
pat=re.compile(expression)
validator=re.search(pat,pASS)

if validator:
    print("\nPassword correcta.\n")
else:

print("\nPassword incorrecta.\n")
