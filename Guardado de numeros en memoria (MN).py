# Convierte un numero a binario, utilizando los metodos de la clase
def Dec_Bin(numero):
    entero = int(numero)
    decimal = numero - entero
    binEntero = bin(entero)[2:]

    # Conversión de la parte decimal a binario
    binDecimal = ""
    while decimal > 0:
        decimal *= 2
        binDigit = int(decimal)
        binDecimal += str(binDigit)
        decimal -= binDigit

    if binDecimal == "":
        return binEntero
    else:
        return binEntero + "." + binDecimal


# PROGRAMA PRINCIPAL
print("1. Guardar numero decimal")
print("2. Ver numero decimal guardado en formato de coma flotante")
opc = int(input())

# Ejecuta la Opcion 1
if (opc == 1):
    num = 0
    mantisaBits = 0
    expBits = 0

    num = float(input("Digite el numero a guardar "))
    mantisaBits = int(
        input("Ingrese la cantidad de bits que se le esignan la mantisa: "))
    expBits = int(
        input("Ingrese la cantidad de bits que se le esignan al exponente: "))

    print(f"El numero será guardado en {mantisaBits+expBits+1} bits.")
    
    # Obtiene el bit del signo, y convierte el numero en su valor absoluto
    if num >= 0:
        signo = "0"
    else:
        signo = "1"
    num = abs(num)

    print(f"El numero en binario es: {Dec_Bin(num)}")
    binList = list(Dec_Bin(num))

    # Encuentra la posicion del punto
    if "." in binList:
        pos = binList.index(".")
    else:
        pos = -1

    # Corre el punto hacia la izquierda si comienza por 1
    if binList[0] == "1":
        dato = binList[1]
        binList[1] = "."
        for i in range(2, len(binList) - 1):
            if binList[i] == ".":
                dato2 = binList[i + 1]
            else:
                dato2 = binList[i]
            binList[i] = dato
            dato = dato2
            e = pos - 1

    # Corre el punto hacia la derecha si comienza por 0
    else:
        pos1 = binList.index("1")
        binList[0] = "1"
        for i in range(1, pos1):
            binList.pop(2)
        e = (pos1 - 1) - (pos1 - 1) * 2

    # Une los elementos de la lista en un solo string
    numero = "".join(binList)

    print(f"Forma normalizada de punto flotante es {numero}x2**{e}")

    exp = Dec_Bin(pos)

    # Rellenar con 0 si el exp tiene menos de 3 cifras
    if len(exp) < expBits:
        for i in range(0, expBits - len(exp)):
            exp = list(exp)
            exp.insert(0, "0")
        exp = "".join(exp)

    # Elimina el entero de la mantisa
    mantisaList = []
    numero = list(numero)
    for x in range(2, len(numero)):
        mantisaList.append(numero[x])
    mantisa = "".join(mantisaList)

    # Rellenar con 0 si la mantisa tiene menos de 3 cifras
    if len(mantisa) < mantisaBits:
        for i in range(0, mantisaBits - len(mantisa)):
            mantisa = list(mantisa)
            mantisa.insert(0, "0")
        mantisa = "".join(mantisa)

    # Limita la mantiza a un numero de cifras
    if len(mantisa) > mantisaBits:
        supr = len(mantisa) - mantisaBits
        supr = supr - (supr * 2)
        mantisa = mantisa[:supr]

    # Calcular el exponente en binario
    exp = Dec_Bin(int((2**expBits - 1) / 2) + e)

    BITS = signo + "-" + exp + "-" + mantisa
    print(BITS)

# Ejecuta la Opcion 2
elif (opc == 2):
    mantisaBits = int(
        input("Ingrese el numero de bits asignado a la mantisa "))
    expBits = int(
        input("Ingrese el numero de bits asignado a los exponentes "))
    comFloat = list(
        str(input("Ingrese el numero binario alamacenado en sistema de coma flotante ")))

    funcionar = False
    # Verificar que los numeros sean binarios
    for i in comFloat:
        if i != "0" and i != "1":
            print(
                "Alguno del los elementos almacenado en coma flotante son diferentes a 0 o 1")
            break
        else:
            funcionar = True

    if (mantisaBits+expBits+1 != len(comFloat)):
        funcionar = False
        print("La cantidad de bits de la mantisa y/o el exponente no correcponden con la cantidad de digitos del numero")

    if (funcionar == True):
        # Asignando los valores a el signo, el exp y la mantisa
        signo = comFloat[0]
        exp = ""
        mantisa = ""
        for i in range(1, expBits+1):
            exp = exp + comFloat[i]
        for i in range(expBits+1, expBits+1+mantisaBits):
            mantisa = mantisa + comFloat[i]

        print(exp)
        print(mantisa)
        # convierte a decimal usando base 2
        expDecimal = int(exp, 2)

        # Enctra el exponente en Decimal
        exp = (int((2**expBits - 1) / 2)-expDecimal)*-1

        # asigna el signo
        if (signo == "1"):
            signo = "-"
        else:
            signo = ""

        print(
            f"Forma normalizada de punto flotante es {signo}1.{mantisa}x2**{exp}")

        # Combina el numero en binario y le coloca e punto
        num = list("1"+mantisa)
        num.insert(exp+1, ".")
        num = "".join(num)

        # Convierte el numero Binario real en decimal real
        # Separa la parte entera de la parte decimal
        partes = num.split(".")
        parteInt = partes[0]
        parteFloat = partes[1]

        # Convierte la parte entera a decimal
        decimalInt = int(parteInt, 2)

        # Convierte la parte decimal a decimal
        decimalFloat = 0
        for i in range(len(parteFloat)):
            decimalFloat += int(parteFloat[i]) * 2 ** -(i+1)

        # Combina los resultados de la parte entera y la parte decimal
        num = decimalInt + decimalFloat

        if (signo == "-"):
            num = num*-1
        print(num)
else:
    print("Numero invalido")
input("Presiona Enter para salir...")

