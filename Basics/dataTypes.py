# La función type te dice qué tipo de dato es la variable

x = 20
print(f"La variable '{x}' es de tipo {type(x)}")
x = 20.5
print(f"La variable '{x}' es de tipo {type(x)}")
x = 1j
print(f"La variable '{x}' es de tipo {type(x)}")
x = "Hello World"
print(f"La variable '{x}' es de tipo {type(x)}")
x = True
print(f"La variable '{x}' es de tipo {type(x)}")
x = ["apple", "banana", "cherry"]
print(f"La variable '{x}' es de tipo {type(x)}")
x = ("apple", "banana", "cherry")
print(f"La variable '{x}' es de tipo {type(x)}")
x = {"name" : "John", "age" : 36}
print(f"La variable '{x}' es de tipo {type(x)}")
x = {"apple", "banana", "cherry"}
print(f"La variable '{x}' es de tipo {type(x)}")
x = range(6)
print(f"La variable '{x}' es de tipo {type(x)}")

# ------------------------------- CASTING -------------------------------
# ----- Podemos cambiar el tipo de dato de algunas variables o datos -----

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'