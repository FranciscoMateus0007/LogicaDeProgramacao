# Inicio

# Leia Desconto, Mercadoria (Entrada Manual / Teclado)
Percentual = float(input("O desconto é: "))
Preço = float(input("O valor da mercadoria é: "))

# Valor <-- Percentual * Preço (Processamento / Atribuição)
Desconto = Percentual * Preço
Valor = Preço - Desconto

# Escreva Desconto, Valor (Saída de danos / Tela)
print(f"O desconto foi de: {Desconto:.2f}")
print(f"O valor total foi de: {Valor:.2f}")

# Fim