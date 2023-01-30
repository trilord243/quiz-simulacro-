infraction={ 1:{"name":"Choque", "cost":50}, 2:{"name":"Semáforo", "cost":30}, 3:{"name":"Falta de documentos", "cost":100}, }

officers={ 1:{"name":"Luis", "lastName":"Bello","ci":13452224}, 2:{"name":"Jose", "lastName":"Quevedo","ci":44235611}, 3:{"name":"Antonio", "lastName":"Guerra","ci":12345678}, }
menu="""   Bienvenido al sistema fiscal de multas Porfavor Selecione una opcion para continuar
          1. Ingresar una infractor
          2.Eliminar un infractor
          3.Mostar las multas registradas
          
          Para salir del menu ingrese otra teclaa que no este en las opciones 
          
          
          
          
          
          """
db={}

validacion=True
while  validacion:
    opciones=["1","2","3"]
    print(menu)
    
    opcion=input("Ingrese una opcion: ")
    
    if opcion in opciones and opcion.isdigit():
        if opcion=="1":
            
            name=input("Ingrese el nombre;")
            apellido=input("Ingrese el apellido; ")
            cedula=input("Ingrese la cedula;")
            tipo=input("Tipo de infraccion: ")
            fiscal_transito=input("El fiscal:  ")
            
            
    else:
        
        validacion=False
        
    
    
    
 
    