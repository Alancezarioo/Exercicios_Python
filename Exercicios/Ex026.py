#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input("Digite Uma Frase: ")).strip().upper()

print("A letra A aparece {} vezes".format(nome.count[A]))
print("A Primeira Letra A Aparece Na {} possição".format(nome.find ('A')+1))
print("A Ultima Letra A Aparece Na {} possição".format(nome.rfind ('A')+1)) 
