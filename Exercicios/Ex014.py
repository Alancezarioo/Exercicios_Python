#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

n1 = float(input("Informe A Temperatura Em °C:"))
n2 = (9*n1/5) + 32
print("A Temperatura de {}ºC,Corresponde A {}ºF".format(n1,n2))