#Pide al usuario dos enteros a y b 
# e imprime todos los números primos entre a y b.


import math


a = int(input("Dime el mínimo: "))
b = int(input("Dime el máximo: "))
esPrimo = True

for n in range(a,b):
    esPrimo = True
    for x in range(2, int(math.sqrt(n) + 1 )):
        if(n % x == 0):
            esPrimo = False
        
    if(esPrimo):
        print(n)
    
