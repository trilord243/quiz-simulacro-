
palabras_censuradas=["racismo", "terrorista", "peligro", "miedo", "odio"]
frase="sdas"


def censurar(oracion,palabrascen):
    for i in palabrascen:
        
        oracion=oracion.replace(i,"*"*len(i))
    return oracion

oracion=input("Ingresa una frase: ").lower()


print(censurar(oracion,palabras_censuradas))


