print(" - Programa que convierte todos los números de una lista de enteros a positivos -")
lista = [-1342,43,547,-345,-2354,234,-235,-34,325]
print("Lista original:", lista)

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] *= -1

print("Nueva lista:", lista)

# - El código de abajo, parece que sirve, pero no -
# for x in lista:
#     if x < 0:
#         x *= -1
# print("Nueva lista:", lista)