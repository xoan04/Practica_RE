import re 
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):  
  
    
    
    if(re.search(regex,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")  
      
  
if __name__ == '__main__' :  
      
    
    email =input("Ingrese el email:")
      
    
    check(email) 
  
    email =input("Ingrese el email:")
    check(email) 
  
    email =input("Ingrese el email:")
    check(email) 