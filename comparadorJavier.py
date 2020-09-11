from datetime import datetime
def javierComparador(a,b):
  print(datetime.now())
  tipoA= type(a)
  print("tipo entrada a:", tipoA)
  if tipoA != type("string") :
    print("tipo no valido")
  tipoB= type(b)
  print("tipo entrada b", tipoB)
  if tipoB != type("string"):
    print("tipo no valido")
  lenA= len(list(a))
  print("largo entrada a es:", lenA)
  lenB= len(list(b))
  print("largo entrada b es:", lenB)
  dif = lenA - lenB 
  print("la diferencia absoluta es:", abs(dif))
  
  if dif>0:
    print(a,b,"el primero es mas largo")
  elif dif<0:
    print(a,b,"el segundo es mas largo")
  else:
    print(a,b,"tienen el mismo largo")


p =input("primera entrada: ")
s =input("segunda entrada: ")
javierComparador(p,s)
