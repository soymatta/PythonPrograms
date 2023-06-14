from numpy import product


def Dis(valor):
    dis = 0.20 # Descuento del 20%
    dis = dis*valor
    valor = valor-dis
    return valor

def Iva(valor):
    iva = 0.19
    iva =valor*iva
    valor = valor+iva
    return valor

prod = float(input("Ingrese el valor de el producto "))
prod = Dis(prod)
print(f"El valor parcial del producto es de ${prod}")
print(f"El valor final del producto es de ${Iva(prod)}")