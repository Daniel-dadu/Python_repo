cadena = input("- Programa que determina si una letra está en un string -\nDame la cadena: ")
caracter = input("Dame el caracter que buscas: ")
if caracter in cadena:
    print(f"El caracter {caracter} sí está en la cadena: '{cadena}'")
else:
    print(f"El caracter {caracter} no está en la cadena: '{cadena}'")
