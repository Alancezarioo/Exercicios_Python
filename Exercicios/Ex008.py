#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input("Um Distancia Em Metros:"))

km = n1 / 10000
hm = n1 / 1000
dan = n1 / 100
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print("A Medida De {} correponde a:".format(n1))

print("km: {}".format(km))
print("hm: {}".format(hm))
print("dan: {}".format(dan))
print("dm: {}".format(dm))
print("cm: {}".format(cm))
print("mm: {}".format(mm))


