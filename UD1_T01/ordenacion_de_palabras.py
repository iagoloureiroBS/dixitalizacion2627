# El usuario introduce una frase. 
# Muestra las palabras ordenadas alfabéticamente y por longitud.

import re

frase = input("Por favor, introduce una frase: ")
    
palabras = re.findall(r'\b\w+\b', frase)
    
if not palabras:
        print("No se encontraron palabras válidas en la frase.")
    

alfabetico = sorted(palabras, key=lambda x: x.lower())
    
por_longitud = sorted(palabras, key=lambda x: (len(x), x.lower()))

print("\n--- Resultados del análisis ---")
print(f"• Palabras detectadas: {palabras}")
print(f"• Orden alfabético:    {alfabetico}")
print(f"• Orden por longitud:  {por_longitud}")
