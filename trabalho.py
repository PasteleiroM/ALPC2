import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
memoria = ['x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', 'x', ' ', 'x', ' ']
#for i in range(100):
#    if(random.randint(0,11) >= 5):
#        memoria[i] = 'x'
#    else:
#        memoria[i] = ' '
#print(memoria)
#Aqui você deve imprimir todo o conteúdo da variável memória
for i in range(0,20):    
    print(memoria[i], end='|')
print()
for i in range(20,40):    
    print(memoria[i], end='|')
print()
for i in range(40,60):    
    print(memoria[i], end='|')
print()
for i in range(60,80):    
    print(memoria[i], end='|')
print()
for i in range(80,100):    
    print(memoria[i], end='|')
print()
while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        try:    
            ini = 0
            while ini < 100:
                if memoria[ini] == ' ':
                    print("Inicio", ini)
                    fim = ini
                    while fim < 100:
                        if memoria[fim + 1] != ' ':
                            break
                        else:
                            fim += 1
                    print("Fim", fim)
                    tamanhoburaco = fim - ini + 1
                    print("Tamanho do buraco:", tamanhoburaco)
                    if tamanhoburaco >= tamanho:
                        print("Tamanho suficiente")
                        for i in range(tamanho):
                            memoria[ini + i] = letra
                            print(memoria, len(memoria))
                        break
                    ini = fim + 1
                ini += 1
        except:
            print("Não há espaço suficiente na memória, tente um item menor")
        pass
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            pass
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                pass
    # Aqui você deve imprimir todo o conteúdo da variável memória
    for i in range(0,20):    
        print(memoria[i], end='|')
    print()
    for i in range(20,40):    
        print(memoria[i], end='|')
    print()
    for i in range(40,60):    
        print(memoria[i], end='|')
    print()
    for i in range(60,80):    
        print(memoria[i], end='|')
    print()
    for i in range(80,100):    
        print(memoria[i], end='|')
    print()