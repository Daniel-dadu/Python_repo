# Pueden ir en comillas simples o dobles:
print("Hello")
print('Hello')

# Strings de varias líneas
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,"""
b = '''sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a + "\n" + b)

# Podemos obtener la longitud de un string con len:
a = "Hello, World!"
print(len(a))

# Con 'in' podemos checar si un string es parte de otro
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("expensive" not in txt)

a = "Hello, World!"
print(a[1])

nums = "0123456"
print(nums[1:3])
print(nums[:-2])
print(nums[-2:])