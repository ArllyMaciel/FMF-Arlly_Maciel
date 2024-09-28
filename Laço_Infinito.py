#autor: Arlly Maciel
#Data: 27/09/2024
#Laço infito while true

while True:
    print("Você está no primeiro laço.")
    opcao1 = input('Deseja sair dele? Digite sim para isso.  ')
    if opcao1 == 'SIM':
        break #Este reak é do primeiro laço
    else:
        while True:
            print("Voce está no segundo laço.")
            opcao2 = input("Deseja sair dele? Digite sim para isso. ")
            if opcao2 == 'SIM':
                break #Este break é do segundo laço
        print("Voce saiu do segundo laço. ")
print("Voce saiu do primeiro laço. ")
