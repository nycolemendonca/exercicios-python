# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

num = int(input("Digite um número: "))


print("O dobro de {} vale {}.".format(num, num*2))
print("O triplo de {} vale {}.".format(num, num*3))
# round() arredonda o resultado para 2 casas decimais
print("A raiz quadrada de {} é igual a {}.".format(num, round(pow(num, 1/2), 2)))
