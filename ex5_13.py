divida_inicial = float(input("Dívida do início: "))
taxa = float(input("Taxa: "))
pagamento = float(input("Pagamento mensal: "))

mes = 0
divida = divida_inicial
total_pago = 0.0

juros_primeiro_mes = (divida_inicial * (taxa / 100))

if pagamento >= juros_primeiro_mes:
    print("PAGAMENTO INSUFICIENTE. DÍVIDA NUNCA SERÁ PAGA.")
else:
    while divida > 0: juros_primeiro_mes = divida * (taxa / 100)
    divida = divida + juros_primeiro_mes
    mes = mes + 1
if divida >= pagamento:
    pago_neste_mes = pagamento
    divida = divida - pagamento
else:
    pago_neste_mes = divida
    divida = 0.0

    total_pago = total_pago = pago_neste_mes
    total_juros = total_pago - divida_inicial

    print(f"mes: {mes}, total pago: {total_pago:.2f}, total de juros: {total_juros:.2f}.")