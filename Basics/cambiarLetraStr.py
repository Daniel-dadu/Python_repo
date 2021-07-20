print(" - Este es un programa que cambia la letra de un string -")
texto = input("Dame un texto: ")
pos = int(input("Dame la posición que quieres cambiar: "))
letra = input(f"La letra de esa posición es '{texto[pos]}', ¿cuál será la nueva letra?: ")
lista = list(texto)
lista[pos] = letra
textoNuevo = "".join(lista)
print("Ahora tu string dice:", textoNuevo)