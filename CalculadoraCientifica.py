import math
import numpy
    
def Sen(num):
    rad = 180/num
    s = numpy.pi/rad
    s = math.sin(s)
    s = round(s, 2)
    return s
    
def Cos(num):
    rad = 180/num
    s = numpy.pi/rad
    s = math.cos(s)
    s = round(s, 2)
    return s
    
def Tan(num):
    rad = 180/num
    s = numpy.pi/rad
    s = math.tan(s)
    s = round(s, 2)
    return s
    
def Exp(num):
    s = math.e
    for i in range(1, num):
        s = s * s
    return s

print("Calculadora cientifica")
opc = 1
while opc <= 6 and opc > 0:
    print("1. Calcular Seno")
    print("2. Calcular Coseno") 
    print("3. Calcular Tangente")
    print("4. Calcular Exponencial")
    print("5. Calcular logaritmo neperiano")
    print("6. Salir")
    opc = int(input())
    if opc == 1:
        print(Sen(float(input("Digite un número "))))
    elif opc == 2:
        print(Cos(float(input("Digite un número "))))
    elif opc == 3:
        print(Tan(float(input("Digite un número "))))
    elif opc == 4:
        print(Exp(float(input("Digite un número "))))
    elif opc == 5:
        print(Log(float(input("Digite un número "))))
    else: print ("Hasta luego")