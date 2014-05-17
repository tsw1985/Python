from Person import Person

def main():
    print("Example code for Python 3.4")
    forExample()
    object()
    
def object():
    person = Person("MyName")
    name = input("Your name??")
    person.setName(name)
    print("Hello " + person.getName())



def forExample():
    listString = ["1","2","3","4","5","6"]
    tupleNumber = (1,2,3,4,5,6)


    for element in listString:
        print ("Element " + element)
        
    for elementNumber in tupleNumber:
        print ("Number %s" % elementNumber)
    
    diccionary = {"key":"value",
                 "tenerife":"Santa Cruz",
                 "españa":"Madrid",
                 "portugal":"Lisboa"
               }
    
    
    print("Diccionary")
    print("Tenerife %s" % diccionary['tenerife'])
    print("España %s"   % diccionary['españa']  )
    
        
   
    
  
    
    
    
    


  
main()

