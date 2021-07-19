print(" - Programa que calcula la media de unos números recibidos en un string -")
digitos = input("Dame unos números: ")
i = 0
suma = 0
while(i < len(digitos)):
    suma += int(digitos[i])
    i += 1
print("La media de los números que ingresaste es", suma/len(digitos))