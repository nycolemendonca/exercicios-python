# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número: "))
a = num - 1
s = num + 1
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(num, (num-1), (num+1)))
