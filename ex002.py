# Entrada de Velocidade
velocidade = float(input("Velocidade (km/h): "))

# Desvio Condicional Composto
if velocidade > 80:
  multa = (velocidade - 80) * 5
  print("Você foi multado!")
  print(f"Multa: R$ {multa:.2f}")
else:
    print("Você não foi multado!")
