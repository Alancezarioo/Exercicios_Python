import math
n1 = float(input("Digite o angulo que voce deseja:"))
s = math.sin(math.radians(n1))
print("o Angulo de {} tem o Seno de {:.2f}".format(n1,s))
c = math.cos(math.radians(n1))
print("o angulo de {} tem o cosseno de {:.2f}".format(n1,c))
t = math.tan(math.radians(n1))
print("o angulo de {} tem o tangente de {:.2f}".format(n1,t))