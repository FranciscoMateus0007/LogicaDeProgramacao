# Constantes do cálculos
custo_dia = 60
custo_km = 0.15

# Entrada de Dados (int e float)
dias = int(input("Dias Alugados: "))
Kms = float(input("Km Rodados: "))

# Processamento e Saída
total = (dias * custo_dia) + (Kms * custo_km)
print(f"Total a pagar: R$ {total:.2f}")
