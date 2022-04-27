import re 
  
expression = re.compile(r"[A-Z][A-Z][A-Z]\d\d\d\d[a-z][a-z][a-z][^a-zA-Z0-9@][^a-zA-Z0-9@][^a-zA-Z0-9@][@]$")
pASS="ABB1111abc#?/@"
pat=re.compile(expression)
mat=re.search(pat,pASS)

if mat:
    print("\nPassword correcta.\n")
else:
    print("\nPassword incorrecta.\n")