print(" - Programa que simula una base de datos de nombres -")
nombres = []
opcion = 1
while(opcion != 0):
    print("\nOpción 1 - Ver los nombres en la base de datos")
    print("Opción 2 - Agregar un nombre a la base de datos")
    print("Opción 3 - Eliminar un nombre de la base de datos")
    print("Opción 0 - Salir del programa")
    opcion = int(input("Ingrese la opción elegida: "))
    if(opcion == 1):
        print("Los nombres de su base de datos son:")
        for nombre in nombres:
            print(nombre, end=" ")
        print()
    elif(opcion == 2):
        op = int(input("Ingresa 1 si quieres insertar un nombre al final o un 2 si deseas insertar el nombre en una posición específica: "))
        nombre = input("Dame el nombre que quiere agregar: ")
        if(op == 1):
            nombres.append(nombre)
        elif(op == 2):
            pos = int(input("Dame la posición en la que quieres insertar el nombre: "))
            nombres.insert(pos, nombre)
    elif(opcion == 3):
        op = int(input("Ingresa 1 si quieres eliminar por nombre o un 2 si deseas eliminar un nombre de una posición específica: "))
        if(op == 1):
            nombre = input("Dame el nombre que quieres eliminar: ")
            nombres.remove(nombre)
        elif(op == 2):
            pos = int(input("Dame la posición del nombre que quieres eliminar: "))
            nombres.pop(pos)
