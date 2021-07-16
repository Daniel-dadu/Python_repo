numero = input("Programa que calcula cuantos dígitos impares hay en un número\nDame el número: ")
i = 0
total = 0
while i < len(numero):
    if int(numero[i])%2 != 0:
        total += 1
    i += 1
print(f"El número {numero} tiene un total de {total} dígitos impares")