a=int(input("Inserte Numero: "))
b=int(input("Inserte Numero: "))
contador=0
for i in range(a,b+1):
   for j in range(1,b+1):
     if i % j == 0:
       contador=contador+1
   if contador==2:
     print(i) 
   contador=0   
