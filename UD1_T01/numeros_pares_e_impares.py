# Solicita al usuario una lista de números separados por espacios y muestra dos listas: una con los pares y otra con los impares.
nums = input("Dime numeros separados por espacios:")
lista_texto = nums.split()
numeros = [int(n) for n in lista_texto]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")