casa = float(input("Valor da casa: R$ "))
renda = float(input("Renda Mensal: R$ "))
anos = float(input("Anos para pagar: "))

prestacao = casa / (anos * 12)

if prestacao > renda * 0.30:
    print(f"Negado! Parcela: R$ {prestacao:.2f}")
else:
    print(f"Aprovado! Parcela R$ {prestacao.2f}")