print(" - Programa que imprime las letras de un string -")
texto = input("Escribe algo: ")
i = 0
print("Las vocales en el texto que me diste son: ", end="")
while i < len(texto):
    if texto[i] in "aeiou":
        print(texto[i], end=" ")
    i += 1