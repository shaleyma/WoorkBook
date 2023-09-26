palabras1 = input("ingresa palabras:  ")
palabras2 = input("ingresa palabras:  ")
palabras3 = input("ingresa palabras:  ")
letra_p = input("Indica una letra: ")

for i in range(len(palabras1)):
  for i in range(len(palabras2)):
    for i in range(len(palabras3)):
      letra1 = palabras1[i - i]
      letra2 = palabras2[i - i]
      letra3 = palabras3[i - i]

if letra_p == letra1 and letra2 and letra3:
  print(palabras1, palabras2, palabras3)
elif letra_p == letra1:
  print(palabras1)
elif letra_p == letra2:
  print(palabras2)
elif letra_p == letra3:
  print(palabras3)
elif letra_p == letra1 and letra2:
  print(palabras1, palabras2)
elif letra_p == letra1 and letra3:
  print(palabras1, palabras3)
elif letra_p == letra2 and letra3:
  print(palabras2, palabras3)
else:
  print("No hay palabra con esta letra")






