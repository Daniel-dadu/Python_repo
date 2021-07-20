print(" - Programa que cambia las letras 's' de un string por '$' -")
texto = input("Dame un texto (preferiblemente que tenga 's'): ")
lista = list(texto)
i = 0
while(i < len(lista)):
    if(lista[i] == "s"):
        lista[i] = "$"
    i += 1

print("Ahora tu texto es:", "".join(lista))