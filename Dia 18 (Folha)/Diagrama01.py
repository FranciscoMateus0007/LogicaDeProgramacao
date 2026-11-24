dia = int(input("Quantidade de dias: "))
km = float(input("Quantidade de kms: "))

preço = (dia * 60) + (km * 0.15)

print(f"Total a pagar: {preço:.2f}")