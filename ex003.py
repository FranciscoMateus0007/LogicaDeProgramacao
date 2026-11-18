salario = float(input("Salário Atual: R$ "))

# Define percentual conforme faixa
if salario > 1250:
    aumento = salario * 0.10
else:
    auemnto = salario * 0.15

    # Saída unificada após o desvio
    novo_salario = salario + aumento
    print(f"aumento: R$ {aummento:.2f}")
    print(f"Novo salário: R$ {novo_salario:2f}")