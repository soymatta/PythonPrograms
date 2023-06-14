nMax = int(input("Ingrese el numero maximo de iteraciones "))
n = 0
fX = int(input("Ingrese el numero a adivinar "))
b = int(input("Ingrese el rango superior "))
a = int(input("Ingrese el rango inferior "))
lastN =b+1

while(n!=nMax):
    n = n+1
    lastN = int((a+b)/2)
    if (fX>lastN):
        a = lastN
    elif (fX<lastN):
        b = lastN
    if (fX == lastN):
        break
    print(lastN)

print(f"Tu numero es {lastN}, encontrado en {n} Iteracciones")