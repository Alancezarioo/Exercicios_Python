#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n1 = input("Digite Algo:")
print("O tipo Do Valor É:", type(n1))
print("É Um Numero?", n1.isnumeric())
print("Tem Espaço?", n1.isspace())
print("É Alfabetico?", n1.isalpha())
print("É Alfa numerico?", n1.isalnum())
print("Ésta Em Minuscula?", n1.islower())
print("Esta Em Maiuscula?", n1.isupper())
print("Esta Capitalizada?", n1.istitle())
