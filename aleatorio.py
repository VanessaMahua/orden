import random
maq=random.randint(1,100)
n=int(input("Adivinalo: "))
contador=1
if n == maq:
  print("Felicitaciones ",contador,"Intentos")
else:
  while maq!=n:
    n=int(input("Adivinalo: ")) 
    print("No lo Es")  
    contador=contador+1
  print("Felicitaciones ",contador,"Intentos")
