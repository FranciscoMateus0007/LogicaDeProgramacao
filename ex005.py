n1 = int(input("1° número: "))
n2 = int(input("2° número: "))
n3 = int(input("3° número: "))

maior = n1
menor = n1

if n2 > maior: maior = n2
if n3 > maior: maior = n3
if n2 < menor: menor = n2
if n3 < menor: menor = n3

print(f"Maior: {maior} | Menor: {menor}")