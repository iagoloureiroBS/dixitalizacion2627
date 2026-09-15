# Escribe un programa que pida al usuario una temperatura en grados Celsius y la convierta a Fahrenheit y Kelvin.
temp = float(input("¿Dime una temperatura?(Celsius)"))
kelvin = temp + 273.15
fahr = (temp * 1.8) + 32
print(f"{temp}Cº equivale a {kelvin}K y {fahr}ºF")