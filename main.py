a = float(input("Digite a medida do lado A do triangulo: \n"))
b = float(input("Digite a medida do lado B do triangulo: \n"))
c = float(input("Digite a medida do lado C do triangulo: \n"))
print(" ")

if (a+b > c) and (a+c > b) and (b+c > a):
  if (a == c) and (a == c) and (b == c):
    print("Equilátero")
  elif (a != c) and (a != c) and (b != c):
    print("Isósceles")
  else:
    print("Escaleno")
    
else:
  print("Não é um triângulo")
