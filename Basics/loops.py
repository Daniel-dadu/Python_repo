# # OJO: Aquí la identación es muy importante

# # Ciclos While:
# i = 1
# while i < 6:
#   print(i, end=" ")
#   i += 1
# print()

# i = 1
# while i < 6:
#   print(i, end=" ")
#   if i == 3:
#     break
#   i += 1
# print()

# # Ciclos for:

# for x in "banana":
#   print(x, end=" ")


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x, end=" ")
# print()

# for x in range(6):
#   print(x, end=" ")
# print()

# for x in range(2, 6):
#   print(x, end=" ")
# print()

# for x in range(2, 33, 3):
#   print(x, end=" ")
# print()

# Ciclos ANIDADOS

# l = [[1,2,3],[4,5,6,10],[7,8,9,11]]
# for i in range(len(l)):
#   for j in range(len(l[0])):
#     print(l[i][j], end=" ")
#   print()

l2 = ["hola", "casa", "malo"]
for i in range(len(l2)):
  for j in range(len(l2[i])):
    if(l2[i][j] == 'a'):
      # print('a', end=" ")
      continue

for i in range(len(l2)):
  for j in range(len(l2[i])):
    print(l2[i][j], end=" ")
  print()
