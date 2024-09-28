#Autor: Arlly Maciel
#Data: 27/09/2024
#Codigos iniciais de repetição

fator = 1
contador = 0
taxa = eval(input("Entre com a raxa de juros anual em porcentagem:   "))
while fator < 1.5:
    fator += fator*taxa/100
    contador += 1
print(f'São necessários {contador} anos para atingir 50% de retabilidade com a taxa de {taxa}% ao ano')
