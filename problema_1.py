numero=input("Ingrese un numero: ")

lista_numeros=[i for i in numero]

lista_numeros_set=set(lista_numeros)

if len(lista_numeros_set)==1:
    print("Es repunit")
else:
    print("No es repunit")



