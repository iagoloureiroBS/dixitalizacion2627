# Pide al usuario una cadena y cuenta cuántas veces aparece cada carácter usando un diccionario.

cadena = input("Dame una cadena de caracteres: ")
cadena.replace(" ", "")
diccionario = {}
for caracter in cadena:
    if caracter in diccionario:
        diccionario[caracter] += 1
    else:
        diccionario[caracter] = 1

print(f"Frecuencia de caracteres: {diccionario}")