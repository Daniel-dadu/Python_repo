# Declarando una lista vacía
lista = []

# Insertando valores en lista
lista.append(1)
lista += [2,3,4,5,59,100]
lista.insert(0, -50) # Primer número es la posición y el segundo es el valor a insertar
print(lista) # Esto imprime: [-50, 1, 2, 3, 4, 5, 59, 100]

# Eliminando valores de lista
lista.pop() # Eliminando el último dato
lista.pop(0) # Eliminando el de la posición 0
lista.remove(59) # Eliminando el 59
print(lista) # Esto imprime: [1, 2, 3, 4, 5]