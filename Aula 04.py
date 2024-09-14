

tempo = float(input("Digite o tempo da viagem:   "))
velocidade = float(input("Digite a velocidade da viagem: "))
distancia = tempo * velocidade
litros_usados = distancia / 12

print("Velocidade Média: ", velocidade)
print("Tempo Gasto: ", tempo)
print("Distancia percorrida: ", distancia)
print("Gasolina utilizada na viagem: ", litros_usados)
