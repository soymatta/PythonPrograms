print("Bienvenido a piedra, papel o tegiras.")
player1 = input("Ingrese el nombre del primer jugador ")
player2 = input("Ingrese el nombre del segundo jugador ")
do = True
while (do):
    do = False
    print(f"Seleccione una opcion para {player1}")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tigeras")
    opc = int(input(""))
    if opc == 1:
        item1 = "Piedra"
    elif opc ==2:
        item1 = "Papel"
    elif opc ==3:
        item1 = "Tigeras"
    elif opc>3 or opc<0:
        print("Digite opcion valida")
        do = True
print(f"{player1} eligió {item1}")
print("")
do = True
while (do):
    do = False
    print(f"Seleccione una opcion para {player2}")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tigeras")
    opc = int(input(""))
    if opc == 1:
        item2 = "Piedra"
    elif opc ==2:
        item2 = "Papel"
    elif opc ==3:
        item2 = "Tigeras"
    elif opc>3 or opc<0:
        print("Digite opcion valida")
        do = True
print(f"{player2} eligió {item1}")
print("")
if item1 == item2:
    print ("Empate")
elif (item1 == "Piedra" and item2 == "Papel") or (item1 == "Papel" and item2 == "Tigeras")or (item1 == "Tigeras" and item2 == "Piedra"):
    print(f"{player2} ganó")
else:
    print(f"{player1} ganó")