# Inicio

# Leia Distância, Velocidade
Distancia = float(input("Quanto foi a distância?: "))
Velocidade = float(input("Quanto foi a velocidade percorrida?: "))

# Tempo <-- Distância / Velocidade (Processamento / Atribuição)
Tempo = Distancia / Velocidade

horas = int(Tempo)
minutos = round((Tempo - horas) * 60)

# Escreva Tempo (Saida de danos / Tela)
if minutos >= 60:
    horas = horas + 1
    minutos = 0

print(f" Tempo de viagem: {horas} horas e {minutos} minutos.")

# Fim