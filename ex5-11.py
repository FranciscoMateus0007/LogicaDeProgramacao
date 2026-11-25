deposito = float(input("Depósito: "))
taxa = float(input("Taxa: "))

mes = 1
saldo = deposito

if mes <= 24:
    rendimento = saldo * (taxa / 100)
    saldo = saldo + rendimento
    print(f" O valor do mês é: {mes + 1} e o saldo é: {saldo}.")

else:
    total_juros = saldo - deposito
    print(f"O total de juros é: {total_juros}")