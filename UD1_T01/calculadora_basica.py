# Implementa una calculadora que acepte dos números y una operación (+, -, *, /) introducidos por consola.
n1 = int(input("Dime el primer num:"))
n2 = int(input("Dime el segundo num:"))
op = input("Escoge operación(+,-,*,/):")

if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
    resultado = n1 * n2
elif op == '/':
    if n2 == 0: print("No es posible dividir entre 0.") 
    else: resultado = n1 / n2
print(f"El resultado es: {resultado}")