# Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm.

num = float(input("Uma distância em metros: "))
print("A medida de {}m corresponde a ".format(num))

km = num * pow(10, -3)
hm = num * pow(10, -2)
dam = num * pow(10, -1)
dm = num * pow(10, 1)
cm = num * pow(10, 2)
mm = num * pow(10, 3)

print("{} km".format(km))
print("{} hm".format(hm))
print("{} dam".format(dam))
print("{} dm".format(dm))
print("{} cm".format(cm))
print("{} mm".format(mm))
